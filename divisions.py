#American League
import pickle

ab_list = pickle.load(open("abbreviation_list.p", "rb"))

#ari, atl, bal, bos, chc, chw, cin, cle, col, det, hou, kcr, laa, lad, mia, mil, min, nym, nyy, oak, phi, pit, sdp, sea, sfg, stl, tbr, tex, tor, wsm           

div_list = ['nl_west', 'nl_east', 'al_east', 'al_east', 'nl_central', 'al_central', 'nl_central', 'al_central', 'nl_west', 'al_central', 'al_west', 'al_central', 'al_west', 'nl_west', 'nl_east', 'nl_central', 'al_central', 'nl_east', 'al_east', 'al_west', 'nl_east', 'nl_central', 'nl_west', 'al_west', 'nl_west', 'nl_central', 'al_east', 'al_west', 'al_east', 'nl_east' ]

div_dict = dict(zip(ab_list, div_list))

