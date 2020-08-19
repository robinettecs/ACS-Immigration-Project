import excel "/Users/christopherrobinette/Desktop/Spring 2020 School Notes/Applied Analytics Project/MAIN DATA/ACS_MERGED_Cleaned_Final.xlsx", sheet("ACS_10") firstrow clear

summarize tot_pop nat_pop fb_pop fb_ntrl_pop fb_nocit_pop

gen pop_minor_tot = unfive_tot + five_svtn_tot
gen pop_minor_nat = unfive_nat + five_svtn_nat
gen pop_minor_fb = unfive_fb + five_svtn_fb
gen pop_minor_fb_ntrl = unfive_fb_ntrl + five_svnt_fb_ntrl
gen pop_minor_fb_nocit = unfive_nocit + five_svnt_fb_nocit

drop unfive_tot five_svtn_tot unfive_nat five_svtn_nat unfive_fb five_svtn_fb unfive_fb_ntrl five_svnt_fb_ntrl unfive_nocit five_svnt_fb_nocit

gen pop_mid_tot = etn_twfr_tot + twfv_ftyfr_tot + ftyfv_fftyfr_tot + fftyfv_sxtfr_tot
gen pop_mid_nat = etn_twfr_nat + twfv_ftyfr_nat + ftyfv_fftyfr_nat + fftyfv_sxtfr_nat
gen pop_mid_fb = etn_twfr_fb + twfv_ftyfr_fb + ftyfv_fftyfr_fb + fftyfv_sxtfr_fb
gen pop_mid_fb_ntrl = etn_twfr_fb_ntrl + twfv_ftyfr_fb_ntrl + ftyfv_fftyfr_fb_ntrl + fftyfv_sxtfr_fb_ntrl
gen pop_mid_fb_nocit = etn_twfr_fb_nocit + twfv_ftyfr_fb_nocit + ftyfv_fftyfr_fb_nocit + fftyfv_sxtfr_fb_noncit


drop etn_twfr_tot etn_twfr_nat etn_twfr_fb etn_twfr_fb_ntrl etn_twfr_fb_nocit twfv_ftyfr_tot twfv_ftyfr_nat twfv_ftyfr_fb twfv_ftyfr_fb_ntrl twfv_ftyfr_fb_nocit ftyfv_fftyfr_tot ftyfv_fftyfr_nat ftyfv_fftyfr_fb ftyfv_fftyfr_fb_ntrl ftyfv_fftyfr_fb_nocit fftyfv_sxtfr_tot fftyfv_sxtfr_nat fftyfv_sxtfr_fb fftyfv_sxtfr_fb_ntrl fftyfv_sxtfr_fb_noncit



gen sxfv_up_tot = sxtyfv_up_tot + combine1_tot + combine2_tot
gen sxfv_up_nat = sxtyfv_up_nat + combine1_nat + combine2_nat
gen sxfv_up_fb = sxtyfv_up_fb + combine1_fb + combine2_fb
gen sxfv_up_fb_ntrl = sxtyfv_up_fb_ntrl + combine1_fb_ntrl + combine2_fb_ntrl
gen sxfv_up_fb_nocit = sxtyfv_up_fb_nocit + combine1_fb_nocit + combine2_fb_nocit

drop sxtyfv_up_tot sxtyfv_up_nat sxtyfv_up_fb sxtyfv_up_fb_ntrl	sxtyfv_up_fb_nocit combine1_tot combine1_nat combine1_fb combine1_fb_ntrl combine1_fb_nocit combine2_tot	combine2_nat combine2_fb combine2_fb_ntrl combine2_fb_nocit





