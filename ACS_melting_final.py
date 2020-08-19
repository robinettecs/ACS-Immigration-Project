import numpy as np
import pandas as pd


ACS_gen = pd.read_csv('ACS_Gen_Trans.csv')
print(ACS_gen)


ACS = pd.read_csv('ACS_Cleaned_Final copy.csv')
print(ACS)


def trans(var):
    #construct string names first to use for lookup in ACS file#
    var = str(var)
    var_name = str(var)
    tot = str(var + '_tot')
    nat = str(var + '_nat')
    fb_ntrl = str(var + '_fb_ntrl')
    fb_nocit = str(var + '_fb_nocit')
    fb = str(var + '_fb')
    print(tot, nat, fb_ntrl, fb_nocit, fb)
    #loop through all column indexes in ACS which correspond to the constructed var names#
    #construct np arrays for each variable cat in sequence
    if tot in ACS:
        tot = np.array(ACS[tot])
    if nat in ACS:
        nat = np.array(ACS[nat])
    if fb_ntrl in ACS:
        fb_ntrl = np.array(ACS[fb_ntrl])
    if fb_nocit in ACS:
        fb_nocit = np.array(ACS[fb_nocit])
    if fb in ACS:
        fb = np.array(ACS[fb])
    else:
        pass
    #reshape the arrays into 1d, then concatenate#
    tot = tot.reshape([336, 1])
    nat = nat.reshape([336, 1])
    fb_ntrl = fb_ntrl.reshape([336, 1])
    fb_nocit = fb_nocit.reshape([336, 1])
    fb = fb.reshape([336, 1])
    var = np.concatenate([tot, nat, fb_ntrl, fb_nocit, fb])
    #convert to data frame, export to csv#
    var = pd.DataFrame(var)
    print(var_name)
    if var_name in ACS_gen:
        ACS_gen[var_name] = var
    print(var)
    print(ACS_gen)
    ACS_gen.to_csv('ACS.csv')
    return ACS_gen

trans('one_race')
trans('white')
trans('black')
trans('amin')
trans('asian')
trans('hwpi')
trans('other')
trans('two_race')
trans('lat_or')
trans('white_only')
trans('hse_mar')
trans('hse_ot')
trans('hse_avg')
trans('fam_avg')
trans('school_3up')
trans('school_pre')
trans('school_k8')
trans('school_high')
trans('school_coll')
trans('educ_twnfv_up')
trans('educ_nohigh')
trans('educ_high')
trans('educ_as')
trans('educ_bach')
trans('educ_grad')
trans('lang')
trans('eng')
trans('no_eng')
trans('some_eng')
trans('empstat')
trans('empstat_inlab')
trans('empstat_civlab')
trans('empstat_civemp')
trans('empstat_civun')
trans('empstat_civun_perc')
trans('empstat_af')
trans('empstat_nolab')
trans('civemp')
trans('wrkcls_wagsal')
trans('wrkcls_govt')
trans('wrkcls_selfemp')
trans('wrkcls_ufw')
trans('occ_mbsa')
trans('occ_srv')
trans('occ_sales')
trans('occ_con')
trans('occ_prod')
trans('ind_agr')
trans('ind_con')
trans('ind_man')
trans('ind_whsale')
trans('ind_retail')
trans('ind_trans')
trans('ind_info')
trans('ind_fire')
trans('ind_psma')
trans('ind_edhc')
trans('ind_aers')
trans('ind_ot')
trans('ind_pa')
trans('popearn12')
trans('earn12_less10')
trans('earn12_10_15')
trans('earn12_15_25')
trans('earn12_25_35')
trans('earn12_35_50')
trans('earn12_50_75')
trans('earn12_75up')
trans('earnmed_m')
trans('earnmed_f')
trans('inc_hh12')
trans('inc_earn12')
trans('inc_earn12_mean')
trans('inc_ss12')
trans('inc_ss12_mean')
trans('inc_ssi12')
trans('inc_ssi12_mean')
trans('inc_cpa12')
trans('inc_rtin12')
trans('inc_fstamp12')
trans('inc_medhh')
trans('avgwrk_hh')
trans('pov12')
trans('povrate_allfam')
trans('povrate_allfam_un18')
trans('povrate_allfam_un5')
trans('novhc')
trans('nophone')
trans('lingisl')
trans('hownperc_less30')
trans('hownperc_up30')
trans('grossrentperc_less30')
trans('grossrentperc_up30')
trans('pop_minor')
trans('pop_mid')
trans('sxfv_up')
trans('m')
trans('f')
