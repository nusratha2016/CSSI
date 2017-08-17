
import webapp2
import json
import logging

import urllib
import urllib2

import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        giphy_data_source = urllib.urlopen(
            "https://maps.googleapis.com/maps/api/directions/json?origin=75+9th+Ave+New+York+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key=AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        #gif_url = parsed_giphy_dictionary[0]
        self.response.write(parsed_giphy_dictionary)

class friendsHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('Friends.html')
        self.response.out.write(main_template.render())
class discoverHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('Discover.html')
        self.response.out.write(main_template.render())



class latlongHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('address.html')
        self.response.out.write(main_template.render())
    def post(self):
        o_address = self.request.get("o_address")
        d_address = self.request.get("d_address")
        logging.info("QUERY:" + o_address)
        #query = self.request.get('q')
        #logging.info("QUERY:" + query)

        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        url_params = {'address': o_address,'key': 'AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08'}

        geocode_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data = json.loads(geocode_response)
        logging.info(json_data['results'][0]['geometry']['location'])
        o_template_dicts = json_data['results'][0]['geometry']['location']

        url_params = {'address': d_address,'key': 'AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08'}

        geocode_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data = json.loads(geocode_response)
        logging.info(json_data['results'][0]['geometry']['location'])
        d_template_dicts = json_data['results'][0]['geometry']['location']


        lat_template = env.get_template('mapdir.html')

        base_url = "https://api.uber.com/v1.2/estimates/price?"
        url_params = {'start_latitude': o_template_dicts['lat'], 'start_longitude': o_template_dicts['lng'], 'end_latitude':d_template_dicts['lat'] ,'end_longitude': d_template_dicts['lng']}

        r = urllib2.Request(base_url + urllib.urlencode(url_params))
        r.add_header("Authorization", "Token mdLSqYtUTVL6S346q4HbdGChonPo7GlItyB4feBI")
        r.add_header("Content-Type", "application/json")
        r.add_header("Accept-Language", "en_EN")

        resp = urllib2.urlopen(r)
        resp_data = resp.read()
        resp_dict = json.loads(resp_data)
        prices = resp_dict['prices']
        string_prices=''
        for item in prices:
            string_prices= string_prices + "<br/>" + item['localized_display_name'] + " " + str(item['low_estimate']) + "-" + str(item['high_estimate']) + " "

        template_dicts = {'o_lat': o_template_dicts['lat'], 'o_long' : o_template_dicts['lng'], 'd_lat':d_template_dicts['lat'], 'd_long' : d_template_dicts['lng'], 'uber_quote': string_prices}
        self.response.write(lat_template.render(template_dicts))

        #request_str='/mapdir?lat=%s&lng=%s' % (d_template_dicts['lat'],d_template_dicts['lng'])
        #self.redirect(request_str)

class UberHandler(webapp2.RequestHandler):
    def get(self):
        #main_template = env.get_template('address.html')
        #self.response.out.write(main_template.render())

        #query = self.request.get('q')
        #logging.info("QUERY:" + query)
        base_url = "https://api.uber.com/v1.2/estimates/price?"
        url_params = {'start_latitude': "40.6631115", 'start_longitude': "-73.9565514", 'end_latitude':"40.6653747" ,'end_longitude': "-73.9654139"}

        r = urllib2.Request(base_url + urllib.urlencode(url_params))
        r.add_header("Authorization", "Token mdLSqYtUTVL6S346q4HbdGChonPo7GlItyB4feBI")
        r.add_header("Content-Type", "application/json")
        r.add_header("Accept-Language", "en_EN")

        resp = urllib2.urlopen(r)
        resp_data = resp.read()
        resp_dict = json.loads(resp_data)
        prices = resp_dict['prices']
        string_prices=''
        for item in prices:
            string_prices=string_prices + item['localized_display_name'] + " " + str(item['low_estimate']) + " " + str(item['high_estimate']) + " "
        self.response.write(string_prices)


class MapHandler(webapp2.RequestHandler):
    def get (self):
        lat = self.request.get('lat')
        lng = self.request.get('lng')
        template_values = {'name':'YOUR_USER_NAME', 'lat': lat, 'lng': lng}

        template = env.get_template('map.html')
        self.response.write(template.render(template_values))



class GipHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'cristiano ronaldo', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}

        giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data =json.loads(giphy_response)
        img_url = json_data['data'][0]['images']['original']['url']
        template_vars= {'url': img_url}

        main_template = env.get_template('abby.html')
        self.response.out.write(main_template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/foooo', MainHandler),
    ('/gip', GipHandler),
    ('/', latlongHandler),
    ('/map', MapHandler),
    ('/uber', UberHandler),
    ('/friends',friendsHandler),
    ('/discover', discoverHandler)
], debug=True)
