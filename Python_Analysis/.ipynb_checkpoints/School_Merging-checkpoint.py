import geopy.distance as geodesic
import pickle
import random
import os

import pandas
##########################################################################################
################################# SETUP ##################################################
##########################################################################################

os.chdir("/Users/rjia/Dropbox/Insight/Patrick_Schools")

lat_delta_mile = 0.02
lon_delta_mile = 0.025

#Get Schools
charter_schools = pickle.load(open("Charter_Schools.pkl", 'rb'))
public_schools = pickle.load(open("Public_Schools.pkl", 'rb'))

#Create school weights
public_schools['gs_weight'] = pandas.to_numeric(public_schools.gs_Rating) * pandas.to_numeric(public_schools.enrollment)
public_schools['ps_weight'] = pandas.to_numeric(public_schools.parentRating) * pandas.to_numeric(public_schools.enrollment)

charter_schools_dict = pandas.DataFrame.to_dict(charter_schools)
public_schools_dict = pandas.DataFrame.to_dict(public_schools)

#def schools_distance(charter_schools_dict, public_schools_dict, range = 3):
range = 3
charter_schools_dict["public_schools_in_range_gs_weight"] = {}
charter_schools_dict["public_schools_in_range_ps_weight"] = {}
charter_schools_dict["public_schools_in_range_total"] = {}
charter_schools_dict["neighborhood_GS_score"] = {}
charter_schools_dict["neighborhood_PS_score"] = {}

for charter in charter_schools_dict["School"]:
	print(charter)
	charter_schools_dict["public_schools_in_range_gs_weight"][charter] = 0
	charter_schools_dict["public_schools_in_range_ps_weight"][charter] = 0
	charter_schools_dict["public_schools_in_range_total"][charter] = 0
	c_loc = (charter_schools_dict["Latitude"][charter], charter_schools_dict["Longitude"][charter])

	for public in public_schools_dict["School"]:
		p_loc = (public_schools_dict["Latitude"][public], public_schools_dict["Longitude"][public])

		if not ('No Data' in c_loc or "No Data" in p_loc):

#			test_lat_delta = abs(float(c_loc[0]) - float(p_loc[0]))
#			test_lon_delta = abs(float(c_loc[1]) - float(p_loc[1]))

			#Do a dummy test on distance
#			if not (lat_delta_mile > (test_lat_delta/range)) and not (lon_delta_mile > (test_lon_delta/range)):

			distance = geodesic.geodesic(p_loc, c_loc).mi
			if distance <= range:
				charter_schools_dict["public_schools_in_range_gs_weight"][charter] += public_schools_dict["gs_weight"][public]
				charter_schools_dict["public_schools_in_range_ps_weight"][charter] += public_schools_dict["ps_weight"][public]
				charter_schools_dict["public_schools_in_range_total"][charter] += float(public_schools_dict["enrollment"][public])
				#print(charter_schools_dict["public_schools_in_range_total"][charter])

	if charter_schools_dict["public_schools_in_range_total"][charter] > 0:
		charter_schools_dict["neighborhood_GS_score"][charter] = charter_schools_dict["public_schools_in_range_gs_weight"][charter]/charter_schools_dict["public_schools_in_range_total"][charter]
		charter_schools_dict["neighborhood_PS_score"][charter] = charter_schools_dict["public_schools_in_range_ps_weight"][charter]/charter_schools_dict["public_schools_in_range_total"][charter]
	else:
		charter_schools_dict["neighborhood_GS_score"][charter] = 'NA'
		charter_schools_dict["neighborhood_PS_score"][charter] = 'NA'

School_Neighbors = pandas.DataFrame.from_dict(charter_schools_dict)

pickle.dump(School_Neighbors, open( "School_Neighbors.pkl", "wb" ) )




#Remove all person
################################################################################
################################# SANDBOX ######################################
################################################################################




################################################################################
############################# Build our functions ##############################
################################################################################
