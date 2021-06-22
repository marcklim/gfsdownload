import os

years=['2016', '2015', '2014', '2013', '2012', '2011', '2010']
days=['0516','0517','0518','0519','0520','0521','0522','0523','0524','0525','0526','0527','0528','0529','0530','0531','0601','0602','0603','0604','0605','0606','0607','0608','0609','0610','0611','0612','0613','0614','0615','0616','0617','0618','0619','0620','0621','0622','0623','0624','0625','0626','0627','0628','0629','0630','0701','0702','0703','0704','0705','0706','0707','0708','0709','0710','0711','0712','0713','0714','0715','0716','0717','0718','0719','0720','0721','0722','0723','0724','0725','0726','0727','0728','0729','0730','0731','0801','0802','0803','0804','0805','0806','0807','0808','0809','0810','0811','0812','0813','0814','0815','0816','0817','0818','0819','0820','0821','0822','0823','0824','0825','0826','0827','0828','0829','0830','0831']
times=['0000', '0600', '1200', '1800']
fields = '-e \':PRMSL:\' -e \':TMP:surface:\' -e \':UGRD:10 m above ground:\' -e \':VGRD:10 m above ground:\''
datafolder = './data/'

# data pre may 2017
# https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/202005/20200514/gfsanl_3_20200514_0000_000.inv
# https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/202005/20200514/gfsanl_3_20200514_0000_000.grb

# data pre may 2020
# https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/202005/20200514/gfsanl_3_20200514_0000_000.inv
# https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/202005/20200514/gfsanl_3_20200514_0000_000.grb2

# data post may 2020
# https://www.ncei.noaa.gov/data/global-forecast-system/access/grid-004-0.5-degree/analysis/202105/20210501/gfs_4_20210501_0000_000.grb2.inv
# https://www.ncei.noaa.gov/data/global-forecast-system/access/grid-004-0.5-degree/analysis/202105/20210501/gfs_4_20210501_0000_000.grb2

for y in years:
    print(y)
    for d in days: 
        for t in times: 
            if (int(y) > 2019):
                m = d[0:2]
                templateurl = 'https://www.ncei.noaa.gov/data/global-forecast-system/access/grid-004-0.5-degree/analysis/yyyymm/yyyydddd/gfs_4_yyyydddd_tttt_000'
                url = templateurl.replace('yyyy', y)
                url = url.replace('mm', m)
                url = url.replace('dddd', d)
                url = url.replace('tttt', t)
                invurl = url  + '.grb2.inv'
                grburl =  url  + '.grb2'
                out = datafolder + grburl.split('/')[len(grburl.split('/'))-1]
            elif (int(y) > 2016):
                m = d[0:2]
                templateurl = 'https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/yyyymm/yyyydddd/gfsanl_3_yyyydddd_tttt_000'
                url = templateurl.replace('yyyy', y)
                url = url.replace('mm', m)
                url = url.replace('dddd', d)
                url = url.replace('tttt', t)
                invurl = url  + '.inv'
                grburl =  url  + '.grb2'
                out = datafolder + grburl.split('/')[len(grburl.split('/'))-1]
            else:
                m = d[0:2]
                templateurl = 'https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/yyyymm/yyyydddd/gfsanl_3_yyyydddd_tttt_000'
                url = templateurl.replace('yyyy', y)
                url = url.replace('mm', m)
                url = url.replace('dddd', d)
                url = url.replace('tttt', t)
                invurl = url  + '.inv'
                grburl =  url  + '.grb'
                out = datafolder + grburl.split('/')[len(grburl.split('/'))-1]

            command = ('./noaa_tools/get_inv.pl ' + invurl + ' | grep ' + fields + ' | ./noaa_tools/get_grib.pl ' + grburl + ' ' + out)



            os.system(command)

