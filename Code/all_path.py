# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:42:29 2021

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:09:37 2021

@author: hp
"""
import cv2
from PIL import Image
#import bellman_ford2
#bellman_ford2.singal_get_path()

if __name__=='__main__':
    img = cv2.imread('./bistu.jpg')      
   # img=cv2.resize(img,((1316,903)),interpolation=cv2.INTER_LINEAR)
    coordinate={
           0: (569, 557),
           1: (1823, 491),
           2: (2651, 454),
           3: (3067, 446),
           4: (3629, 432),
           5: (3799, 1409),
           6: (3661, 1409),
           7: (3129, 1409),
           8: (2960, 1391),
           9: (2847, 1188),
           10: (2676, 1073),
           11: (2004, 1070),
           12: (1606, 1494),
           13: (1383, 1512),
           14: (1052, 1524),
           15: (1621, 2634),
           16: (2808, 2763),
           17: (4329, 2833),
           18: (1855, 620),
           19: (2666, 572),
           20: (3056, 557),
           21: (3060, 1033),
           22: (3593, 1037),
           23: (1805, 1512),
           24: (2971, 1520),
           25: (2987,1794),
           26: (2936, 1900),
           27: (1802, 1826),
           28: (1823, 1900),
           29: (1958, 2177),
           30: (2850, 2177),
           31: (3469, 1915),
           32: (3465, 2184),
           33: (1990, 2317),
           34: (1994, 2486),
           35: (2815, 2368),
           36: (2811, 2549),
           37: (1386, 1878),
           38: (1713, 2468),
           39: (3472, 2597),
           40: (3828, 1915),
           41: (4094, 2645),
           42: (1368, 1081),
           43: (1955, 955),
           44: (1795, 1664),
           45: (1811,1291),
           46: (1835,1307),
           47: (1752,1366),
           48: (2549,1547),
           49:(4266,929),#比例尺
           50:(4556,929),#比例尺
           51:(2396,1324),
           52:(2429,1483),
           53:(2969,1478),
           54:(2429,1544),
           55:(1435,1157),
           56:(1501,1157),
           57:(1742,1188),
           58:(1584,1258),
           101:(1938, 1310),# 自动化学院主入口
            102:(1961,1314),
            103:(1955,1367),
            104:(1904,1366),
            105:(1830,1364),
            106:(1792,1367),
            108:(1959,1385),
            109:(2091,1386),
            110:(2091,1346),
            111:(2093,1236),
            112:(1986,1267),
            113:(2018,1241),
            114:(2062,1228),
            115:(2133,1236),
            116:(2133,1154),
            117:(2132,1080),
            118:(2278,1133),
            119:( 2288,1078),
            120:(2090,1454),
            121:(2066,1516),
            122:(2093,1406),
            123:(2165,1410),
            124:(2163,1506),
            125:(2271,1411),#机电学院主入口
            126:(2305,1412),
            127:(2307,1326),
            128:(2373,1323),
            129:(2375,1263),
            130:(2377,1204),
            131:(2372,1236),
            132:(2374,1079),
            133:(1829,1396),
            134:(1828,1514),
            135:(2057,1467),#光电学院主入口（未在图片中）
            136:(2372,1127),
            137:(2400,1126),
            138:(2401,1107),
            139:(2455,1105),
            140:(2498,1110),
            141:(2541,1119),
            142:(2600,1137),
            143:(2599,1082),
            144:(2601,1258),
            145:(2577,1322),
            146:(2508,1322),
            147:(2507,1262),
            148:(2479,1263),
            149:(2479,1233),
            150:(2524,1263),
            151:(2525,1236),
            152:(2580,1235),
            153:(2604,1236),
            154:(2578,1356),
            155:(2592,1368),
            156:(2591,1470),
            157:(2761,1470),
            158:(2395,1381),
            159:(2417,1321),
            160:(2443,1265),
            161:(2468,1321),
            162:(2470,1356),
            163:(2715,1478),
            164:(2714,1543),
            165:(2869,1541),
            166:(2965,1541),
            167:(2966,1651),
            168:(2867,1644),
            169:(2865,1838),
            170:(2713,1836),
            171:(2777,1842),
            172:(2651,1843),
            173:(2652,1909),
            174:(2773,1912),
            175:(2570,1839),
            176:(2572,1547),
            177:(2497,1546),
            178:(2496,1903),
            179:(2546,1479),
            180:(2241,1624),
            181:(2208,1642),
            182:(2069,1643),
            183:(1933,1643),
            184:(1877,1651),
            185:(1862,1637),
            186:(1797,1638),
            187:(1947,1677),
            188:(1989,1671),
            189:(2066,1671),
            190:(2072,1749),
            191:(2029,1753),
            192:(1936,1751),
            193:(2081,1902),
            194:(2039,1899),
            195:(2032,1835),
            196:(2080,1935),
            197:(1888,1896),
            198:(1888,1841),
            199:(2149,1896),
            200:(2420,1514),
            201:(2132,1997),#学一食堂(H1)主入口2
            202:(2066,1963),#学一食堂(H2)主入口
            203:(2081,1902),
            204:(2141,2114),#学一食堂（H1）主入口1
            205:(2143,2178),
            206:(2021,2043),#学一食堂(H1)货口
            207:(1962,2059),
            208:(1908,2091),
            209:(2064,1995),
            210:(1894,1901),
            211:(1874,1956),
            212:(1905,1951),#学一食堂(H2)
            213:(1841,1965),
            214:(2715,1916),
            215:(2716,2181),
            216:(2502,2179),
            217:(1990,2340),
            218:(2290,2179),
            219:(2286,2513),
            220:(2606,2181),
            221:(2636,2306),
            222:(2633,2541),
            223:(2810,2303),
            224:(3154,1914),
            225:(3151,2179),
            226:(),
            227:(3150,2586),
            228:(3148,2061),
            229:(2947,2121),
            230:(),
            231:(3058,1792),#学生科技活动创新教育中心
            232:(2970,1609),
            233:(3661,1914),#风雨操场与后勤保障中心
            234:(3582,1604),
            235:(3508,1413),
            236:(3730,1585),
            237:(3602,1708),
            238:(3761,1709),
            239:(3038,772),
            240:(2658,777),
            241:(3325,773),
            242:(3323,547),
            243:(2811,772),#产业研发大楼（远期）
            244:(3441,772),#国际交流中心
            245:(3325,1044),
            246:(3122,1346),
            247:(3640,1332),
            248:(3570,1326),
            249:(3390,1407),
            250:(3400,1319),
            251:(3321,1410),
            252:(3323,1319),
            253:(3004,1030),
            254:(2207,599),
            255:(2209,767),
            256:(2203,643),#预留教学实验用地
            257:(1544,1408),#学生三食堂
            258:(1602,1368),
            259:(1602,1261),
            260:(1673,1261),
            261:(1674,1189),
            262:(1850,1190),
            263:(1740,1086),#研究生宿舍/倒班宿舍（远期）s13
            264:(1895,1087),#后勤服务楼（远期）
            265:(1501,1257),
            266:(1429,1257),
            267:(1368,1264),
            268:(1358,1343),
            269:(1238,1340),
            270:(1231,1177),#工程训练车辆中心
            271:(1219,1116),
            272:(1137,1132),
            273:(1586,1121),#研究生宿舍/留学生宿舍s11
            274:(1672,1122),
            275:(1800,1743),
            276:(1756,1743),#篮球场1
            277:(1393,1649),
            278:(1340,1656),
            279:(1861,2108),#足球场1
            280:(1649,2354),
            281:(1677,2352),#燃气调压站
            282:(),
            283:(1778,2474),
            284:(1778,2446),#锅炉房
            285:(1910,2482),
            286:(1908,2437),#网球场
            287:(2303,776),
            288:(2307,862),
            289:(2301,933),
            290:(2504,862),
            291:(2511,939),
            292:(2811,740),
            293:(3328,685),
            294:(3444,744)
    }
    g={
            
            '0':{'1':1255.7,'14':1080.9},
            '1':{'0':1255.7,'2':828.8,'18':132.9},
            '2':{'1':828.8,'3':416.6,'19':118.9},
            '3':{'2':416.6,'4':562.2,'20':111.5},
            '4':{'3':562.2,'5':991.7},
            '5':{'4':991.7,'6':138,'17':1519.4,'236':189},
            '6':{'40':532.8,'5':138,'235':153.1,'236':189,'247':79.8,'248':123.3,'249':271,'7':594.1,'251':340,'22':378.2},
            '7':{'8':159,'246':63.4,'251':192,'6':532},
            
            
            '8':{'53':72,'7':159,'9':250.3,'24':114,'166':135.1,'235':538},
            '9':{'8':232.3,'10':206.7},
            '10':{'9':206.7,'11':672,'19':501.1,'143':77.5,'240':296.5,'132':302.1},
            '11':{'10':672,'43':125,'117':128.4,'11':195.2},
            '12':{'13':223.7,'44':254.2,'257':106,'258':126.1,'262':389.9,'45':267,'47':194.2},
            '13':{'12':223.7,'14':331.2,'42':476.7,'37':366,'268':170.8,'277':137.4},
            '14':{'13':331.2,'15':1247.3,'0':1080.9},
            '15':{'14':1247.3,'16':1194},
            '16':{'15':1194,'17':1522.6,'36':214},
            '17':{'16':1522.6,'5':1519.4},
            '18':{'254':352.6,'1':132.9,'19':812.4,'43':349.6},
            '19':{'2':132.9,'18':812.4,'10':501.1,'20':390.3,'254':459.8,'240':205.2},
            '20':{'3':111.5,'21':476,'19':390.3,'242':267.2,'239':215.8},
            '21':{'253':56.1,'245':265.2,'239':262},
            '22':{'6':378.2,'21':533,'245':268.1,'247':298.7},
            '23':{'27':314,'24':1166,'44':152.3,'186':126.3,'134':23.1,'23':196,'106':145.6},
            '24':{'8':114,'166':21.8,'200':551,'53':42},
            '25':{'26':117.6,'167':144.5,'231':71},
            '26':{'25':166.4,'28':1113,'30':290,'31':533.2,'174':163.4,'224':218,'229':221},
            '27':{'28':76.9,'23':314,'44':162.2},
            '28':{'27':76.9,'26':1113,'29':308.1,'197':65.1,'213':64},
            '29':{'28':308.1,'30':892,'33':143.6,'205':185,'208':99.5,'217':166.1},
            '30':{'26':290,'32':615,'35':194.2,'29':892,'215':134.1,'223':132.1,'225':301},
            #截止
            '31':{'32':269,'26':533.2,'40':359,'224':315,'233':192},
            '32':{'31':269,'39':413.1,'30':615},
            '33':{'29':143.6,'34':169},
            '34':{'33':169,'38':281.6,'36':819.4,'217':146.1,'219':293.2,'285':84.1},
            '35':{'30':194.2,'36':181},
            '36':{'16':214,'34':819.4,'35':181,'39':662.7,'222':178,'223':246},
            '37':{'38':674.6,'13':366,'277':229.1,'280':543.8},
            '38':{'34':281.6,'37':674.6,'280':130.7,'283':65.3},
            '39':{'32':413.1,'36':662.7,'41':623.8,'227':322},
            '40':{'6':532.8,'31':359,'41':776.9,'233':167,'238':216.6},
            '41':{'39':623.8,'40':776.9},
            '42':{'13':476.7,'43':600.4,'267':183,'271':153.1},
            '43':{'11':125,'18':349.6,'42':600.5},
            '44':{'12':254.2,'27':162.2,'23':152.3},
            '45':{'12':288.5,'23':221.1,'262':108.3,'46':28.8},
            '46':{'45':28.8,'105':57.2,'47':95.2},
            '47':{'45':95.4,'12':194.2,'106':40},
            '48':{'177':52,'176':23},
            '49':{},
            '50':{},
            '51':{'128':23,'158':57,'159':21.2},
            '52':{'179':117.1,'200':32.3},
            '53':{'24':42,'157':208.2,'8':72},
            '54':{'200':32.3,'177':68},
            '55':{'266':100.2,'56':66},
            '56':{'55':66,'265':100.2},
            '57':{'261':68,'262':108},
            '58':{'273':137,'265':83,'259':18.2},
            '59':{},
            '60':{},
            '61':{},
            '62':{},
            '63':{},
            '64':{},
            '65':{},
            '66':{},
            '67':{},
            '68':{},
            '69':{},
            '70':{},
            '71':{},
            '72':{},
            '73':{},
            '74':{},
            '75':{},
            '76':{},
            '77':{},
            '78':{},
            '79':{},
            '80':{},
            '81':{},
            '82':{},
            '83':{},
            '84':{},
            '85':{},
            '86':{},
            '87':{},
            '88':{},
            '89':{},
            '90':{},
            '91':{},
            '92':{},
            '93':{},
            '94':{},
            '95':{},
            '96':{},
            '97':{},
            '98':{},
            '99':{},
            '100':{},
            '101':{'102':23.3},
            '102':{'101':23.3,'103':53.3,'112':53.3,'110':133.9},
            '103':{'102':53.3,'104':51,'108':18},
            '104':{'103':51,'105':74},
            '105':{'104':74,'106':38.1,'46':57.2,'133':32},
            '106':{'105':38.1,'47':40,'23':145.6},
            '107':{},
            '108':{'103':18,'109':132},
            '109':{'108':132,'122':20.1,'110':40},
            '110':{'109':40,'111':110,'102':133.9},
            '111':{'110':110,'114':32,'115':40},
            '112':{'102':53.3,'113':41.2},
            '113':{'112':41.2,'114':45.9},
            '114':{'111':32,'113':45.9},
            '115':{'111':40,'116':82,'131':239},
            '116':{'115':82,'117':74,'118':146.5},
            '117':{'116':74,'119':156,'11':128.4},
            '118':{'116':146.5,'119':50.9},
            '119':{'117':156,'118':50.9,'132':86},
            '120':{'122':48,'121':66.5,'135':35.5},
            '121':{'120':66.5,'124':97.5,'134':238,'135':49.8,'182':127},
            '122':{'109':20.1,'120':48,'123':72.1},
            '123':{'122':72.1,'125':106,'124':96},
            '124':{'121':97.5,'123':96,'125':143.8,'180':141.4,'181':143.3,'200':257.1},
            '125':{'123':106,'124':143.8,'126':34},
            '126':{'125':34,'127':86},
            '127':{'126':86,'128':66.1},
            '128':{'127':66.1,'129':60,'51':23},
            '129':{'131':27.2,'128':60,'160':68},
            '130':{'131':32.4,'132':125,'136':77.2},
            '131':{'115':239,'129':27.2,'130':32.4},
            '132':{'119':86,'130':125,'10':302.1,'136':48},
            '133':{'105':32,'134':118},
            '134':{'133':118,'121':238,'23':23.1},
            '135':{'120':35.5,'121':49.8},
            '136':{'130':77.2,'137':28,'132':48},
            '137':{'136':28,'138':19},
            '138':{'137':19,'139':54},
            '139':{'138':54,'140':43.3},
            '140':{'141':43.9,'139':43.3},
            '141':{'140':43.9,'142':61.7},
            '142':{'141':61.7,'153':99.1},
            '144':{'153':22.2,'145':68.4,'152':31.1},
            '143':{'10':77.5},
            '145':{'144':68.4,'152':87.1,'154':34,'146':69},
            '146':{'147':60,'145':69,'161':40},
            '147':{'148':28,'150':17,'146':60},
            '148':{'147':28,'160':36.1,'149':30},
            '149':{'148':30,'151':46.1},
            '150':{'147':17,'151':27},
            '151':{'150':27,'152':55,'149':46.1},
            '152':{'151':55,'153':24,'145':87.1,'144':31.1},
            '153':{'152':24,'144':22.2,'142':99.1},
            '154':{'145':34,'155':18.4,'162':108},
            '155':{'154':18.4,'156':102},
            '156':{'155':102,'157':170,'163':124.3},
            '157':{'156':170,'163':46.7,'53':208.2},
            '158':{'51':57},
            '159':{'128':44,'161':51,'160':61.7,'51':21.2},
            '160':{'159':61.7,'129':68,'148':36.1},
            '161':{'159':51,'146':40,'162':35.1},
            '162':{'161':35.1,'154':108},
            '163':{'157':46.7,'164':65,'156':124.3},
            '164':{'163':65,'165':155,'176':142.1},
            '165':{'164':155,'166':96,'168':103},
            '166':{'165':96,'167':110,'8':150.1,'24':21.8},
            '167':{'166':110,'168':99.2,'25':144.5,'232':42.2},
            '168':{'167':99.2,'169':194,'165':103},
            '169':{'168':194,'171':88.1},
            '170':{'171':64.3,'172':62.4},
            '171':{'170':64.3,'169':88.1,'174':77.1},
            '172':{'170':62.4,'175':81.1,'173':66},
            '173':{'172':66,'174':121,'178':156.1,'214':63.4},
            '174':{'173':121,'171':77.1,'26':163.4,'214':58.1},
            '175':{'176':292,'172':81.1},
            '176':{'177':75,'175':292,'164':142.1,'48':23},
            '177':{'178':357,'48':52,'54':68},
            '178':{'177':357,'173':156.1},
            '179':{'156':45.9,'52':117.1},
            '180':{'181':37.6,'124':141.4},
            '181':{'180':37.6,'124':143.3,'182':139},
            '182':{'181':139,'121':127,'189':28.2},
            '183':{'184':56.6,'187':36.8},
            '184':{'183':56.6,'185':20.5},
            '185':{'184':20.5,'186':65},
            '186':{'185':65,'23':126.3,'28':263.3,'275':105},
            '187':{'183':36.8,'188':42.4,'192':74.8,'191':111.8},
            '188':{'187':42.4,'189':77},
            '189':{'188':77,'182':28.2,'190':78.2},
            '190':{'189':78.2,'191':43.2,'196':186.2},
            '191':{'190':43.2,'192':93},
            '192':{'191':93,'187':74.8},
            '193':{'196':33,'194':42.1,'199':68.3,'201':107.8},
            '194':{'193':42.1,'195':64.4,'199':110,'210':145},
            '195':{'194':64.4,'196':110.9,'198':144.1},
            '196':{'195':110.9,'190':186.2,'193':33},
            '197':{'198':55,'28':65.1,'210':14.9},
            '198':{'197':55,'195':144.1},
            '199':{'193':68.3,'201':102.4,'194':110,'202':160.7,'26':787},
            '200':{'54':32.3,'124':257.1,'24':551,'52':32.3},
            '201':{'199':102.4,'193':107.8,'209':68,'202':74.2,'193':107.8},
            '202':{'209':32.1,'193':62.8,'201':74.2,'199':106.7},
            '203':{},
            '204':{'205':64},
            '205':{'204':64,'29':185},
            '206':{'207':61.1},
            '207':{'206':61.1,'208':62.8},
            '208':{'207':62.8,'213':142.7,'29':99.5,'279':50},
            '209':{},
            '210':{'211':58.5,'28':71,'194':145},
            '211':{'210':58.5,'212':31.4,'213':34.2},
            '212':{'211':31.4},
            '213':{'28':67.4,'211':34.2,'208':142.7},
            '214':{'173':63.4,'174':58.1,'215':265},
            '215':{'214':165,'30':134.1,'220':110},
            '216':{'178':276.1,'218':212,'220':104},
            '217':{'29':166.1,'34':146.1},
            '218':{'205':147,'216':212,'219':334},
            '219':{'218':334,'34':293.2,'222':348.1},
            '220':{'216':104,'221':128.5,'215':110},
            '221':{'220':128.5,'223':174,'222':235},
            '222':{'221':235,'219':348.1,'36':178},
            '223':{'221':174,'30':132.1,'36':246},
            '224':{'26':218,'31':315,'228':147.1},
            '225':{'228':118,'227':407,'30':301},#少点
            '226':{},
            '227':{'225':407,'39':322},
            '228':{'224':147.1,'225':118},
            '229':{'30':112,'26':221},
            '230':{},#少点
            '231':{'25':71},
            '232':{'167':42.2,'166':68.2,'234':612},
            '233':{'31':192,'40':167},
            '234':{'237':105.9,'236':149.2,'235':204.8,'232':612},
            '235':{'6':153.1,'234':204.8,'8':548.4},
            '236':{'6':189,'234':149.2,'5':189,'238':127.8},
            '237':{'234':105.9,'238':159},
            '238':{'237':159,'40':216.6,'236':127.8},
            '239':{'20':215.8,'243':227,'241':287,'21':262},
            '240':{'19':205.2,'243':153.1,'10':296.5,'287':355},
            '241':{'245':271,'244':116,'239':287,'293':88.1},
            '242':{'20':267.2,'293':138.1},
            '243':{'240':153.1,'239':227,'292':32},
            '244':{'294':28.2,'241':116},
            '245':{'241':271,'21':265.2,'22':268.1},
            '246':{'7':63.4},
            '247':{'248':70.3,'6':79.8,'22':298.7},
            '248':{'247':70.3,'6':123.2},
            '249':{'6':271,'251':69.1},
            '250':{},
            '251':{'249':69.1,'252':91,'7':192,'6':340},
            '252':{'251':91},
            '253':{'21':56.1},
            '254':{'256':44.2,'19':489.8,'18':352.6},
            '255':{'256':124.1,'287':94.4},
            '256':{'255':124.1,'254':44.2},
            '257':{'258':70.5,'12':106},
            '258':{'257':70.5,'12':126.1,'259':107,'58':18.2},
            '259':{'258':107,'260':71,'265':101.1},
            '260':{'259':71,'261':72},
            '261':{'57':68,'260':72,'274':67,'262':176},
            '262':{'57':108,'11':195.2,'12':389.8,'45':133.8},
            '263':{'264':155,'57':102},
            '264':{'263':155,'11':110.3},
            '265':{'259':101.1,'266':72,'58':83},
            '266':{'265':72,'267':61.4},
            '267':{'266':61.4,'42':183,'268':79.6},
            '268':{'267':79.6,'13':170.8,'269':120},
            '269':{'268':120,'270':163.1},
            '270':{'269':163.1,'271':62.2},
            '271':{'270':62.2,'272':83.5,'42':153.1},
            '272':{'271':83.5},
            '273':{'274':86,'58':137},
            '274':{'273':86,'261':67},
            '275':{'276':44,'186':105,'28':158.7},
            '276':{'275':44},
            '277':{'278':53.5,'37':229.1,'13':137.4},
            '278':{'277':53.5},
            '279':{'208':50},
            '280':{'37':543.8,'281':28.1,'38':130.7},
            '281':{'280':28.1},
            '282':{},
            '283':{'284':28,'38':65.3,'285':132.2},
            '284':{'283':28},
            '285':{'283':132.2,'34':84.1,'286':45},
            '286':{'285':45},
            '287':{'255':94.4,'240':355,'288':86.1},
            '288':{'287':86.1,'290':197,'289':71.3},
            '289':{'288':71.3,'291':210.1},
            '290':{'288':197,'291':77.3},
            '291':{'289':210.1,'290':77.3},
            '292':{'243':32},
            '293':{'241':88.1,'242':138.1},
            '294':{'244':28.2}
            }
            
    for i in g:
        print('')
        for j in g[i]:
            k=[]
            k.append(int(i))
            k.append(int(j))
           # print(k,end='')
            w=[]
            for m in range(len(k)):
                if k[m] in coordinate:
                    w.append(coordinate[k[m]])
            cv2.line(img, w[m-1],w[m],(0, 255, 255),10)
            
           
  
   
    
   # cv2.namedWindow("image")
    #cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    #cv2.imshow("image", img)
    #cv2.waitKey(0)
    cv2.imwrite("./all_path.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    im = Image.open('all_path.jpg')
    im.show()