import re
import requests
from bs4 import BeautifulSoup
import json

# URL of the website you want to scrape
camp5_ou_url = 'https://www.camp5.com/1utama/'
camp5_ut_url = 'https://www.camp5.com/utropolis/'
batuu_url = 'https://www.batuuclimbing.com/pricing'
bump_url = 'https://www.bumpbouldering.com/pricing'
bhub_url = 'https://bhubbouldering.com/plan-pricing/'

# Send a GET request to the website
camp5_ou_response = requests.get(camp5_ou_url)
camp5_ut_response = requests.get(camp5_ut_url)
batuu_response = requests.get(batuu_url)
bump_response = requests.get(bump_url)
bhub_response = requests.get(bhub_url)

data = []
finaldata = []
ignore_list = ["~","KIDS","YOUTH","JUNIOR"]

# Check if the request was successful
if camp5_ou_response.status_code == 200:
    #print(response.text)
    soup = BeautifulSoup(camp5_ou_response.text, 'html.parser')
    
    day_passes = soup.select(".wpb_column.vc_column_container.vc_col-sm-4.vc_col-xs-4")

    categories = day_passes[0].find_all(recursive=False)
    offpeak = day_passes[1].find_all(recursive=False)
    peak = day_passes[2].find_all(recursive=False)
    categories_arr = categories[0].find_all("h2")
    offpeak_arr = offpeak[0].find_all("h3")
    peak_arr = peak[0].find_all("h3")

    for i in range(len(categories_arr)):
        category = categories_arr[i].text
        if category in ignore_list:
            continue
        data.append({
            "key": "Camp5_day_pass_offpeak",
            "category": category,
            "price": offpeak_arr[i].text.replace("MYR","RM")
        })
    for i in range(len(categories_arr)):
        category = categories_arr[i].text
        if category in ignore_list:
            continue
        data.append({
            "key": "Camp5_day_pass_peak",
            "category": category,
            "price": peak_arr[i].text.replace("MYR","RM")
        })

    xs6bulk = soup.select(".wpb_column.vc_column_container.vc_col-sm-6.vc_col-xs-6")

    tenday_pass_categories = xs6bulk[0].find_all(recursive=False)
    tenday_pass_prices = xs6bulk[1].find_all(recursive=False)
    tenday_categories_arr = tenday_pass_categories[0].find_all("h2")
    tenday_prices_arr = tenday_pass_prices[0].find_all("h3")

    for i in range(len(tenday_categories_arr)):
        tenday_category = tenday_categories_arr[i].text
        if tenday_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_tenday_pass",
            "category": tenday_category,
            "price": tenday_prices_arr[i].text.replace("MYR","RM")    
        })

    ou_monthly_passes_categories = xs6bulk[2].find_all(recursive=False)
    ou_monthly_pass_prices = xs6bulk[3].find_all(recursive=False)
    ou_monthly_categories_arr = ou_monthly_passes_categories[0].find_all(["h2","h3"])
    ou_monthly_prices_arr = ou_monthly_pass_prices[0].find_all("h3")
    
    for i in range(len(ou_monthly_categories_arr)):
        ou_monthly_category = ou_monthly_categories_arr[i].text
        if ou_monthly_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_monthly_ou_pass",
            "category": ou_monthly_category,
            "price": ou_monthly_prices_arr[i].text.replace("MYR","RM")
        })
    
    multi_monthly_passes_categories = xs6bulk[4].find_all(recursive=False)
    multi_monthly_pass_prices = xs6bulk[5].find_all(recursive=False)
    multi_monthly_categories_arr = multi_monthly_passes_categories[0].find_all(["h2","h3"])
    multi_monthly_prices_arr = multi_monthly_pass_prices[0].find_all("h3")
    
    for i in range(len(multi_monthly_categories_arr)):
        multi_monthly_category = multi_monthly_categories_arr[i].text
        if multi_monthly_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_monthly_multi_pass",
            "category": multi_monthly_category,
            "price": multi_monthly_prices_arr[i].text.replace("MYR","RM")
        })
    
    three_monthly_ou_passes_categories = xs6bulk[8].find_all(recursive=False)
    three_monthly_ou_pass_prices = xs6bulk[9].find_all(recursive=False)
    three_monthly_ou_categories_arr = three_monthly_ou_passes_categories[0].find_all(["h2","h3"])
    three_monthly_ou_prices_arr = three_monthly_ou_pass_prices[0].find_all("h3")
    
    for i in range(len(three_monthly_ou_categories_arr)):
        t_ou_monthly_category = three_monthly_ou_categories_arr[i].text
        if t_ou_monthly_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_three_month_ou_pass",
            "category": t_ou_monthly_category,
            "price": three_monthly_ou_prices_arr[i].text.replace("MYR","RM")
        })
    
    three_monthly_multi_passes_categories = xs6bulk[10].find_all(recursive=False)
    three_monthly_multi_pass_prices = xs6bulk[11].find_all(recursive=False)
    three_monthly_multi_categories_arr = three_monthly_multi_passes_categories[0].find_all(["h2","h3"])
    three_monthly_multi_prices_arr = three_monthly_multi_pass_prices[0].find_all("h3")
    
    for i in range(len(three_monthly_multi_categories_arr)):
        t_multi_monthly_category = three_monthly_multi_categories_arr[i].text
        if t_multi_monthly_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_three_month_multi_pass",
            "category": t_multi_monthly_category,
            "price": three_monthly_multi_prices_arr[i].text.replace("MYR","RM")
        })
    
    year_ou_passes_categories = xs6bulk[12].find_all(recursive=False)
    year_ou_pass_prices = xs6bulk[13].find_all(recursive=False)
    year_ou_categories_arr = year_ou_passes_categories[0].find_all(["h2","h3"])
    year_ou_prices_arr = year_ou_pass_prices[0].find_all("h3")
    
    for i in range(len(year_ou_categories_arr)):
        year_ou_category = year_ou_categories_arr[i].text
        if year_ou_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_year_ou_pass",
            "category": year_ou_category,
            "price": year_ou_prices_arr[i].text.replace("MYR","RM")
        })
    
    year_multi_passes_categories = xs6bulk[14].find_all(recursive=False)
    year_multi_pass_prices = xs6bulk[15].find_all(recursive=False)
    year_multi_categories_arr = year_multi_passes_categories[0].find_all(["h2","h3"])
    year_multi_prices_arr = year_multi_pass_prices[0].find_all("h3")
    
    for i in range(len(year_multi_categories_arr)):
        year_multi_category = year_multi_categories_arr[i].text
        if year_multi_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_year_multi_pass",
            "category": year_multi_category,
            "price": year_multi_prices_arr[i].text.replace("MYR","RM")
        })
    
else:
    print(f'Failed to retrieve the webpage. Status code: {camp5_ou_response.status_code}')

if camp5_ut_response.status_code == 200:
    soup = BeautifulSoup(camp5_ut_response.text, 'html.parser')
    
    ut_day_passes = soup.select(".wpb_column.vc_column_container.vc_col-sm-4.vc_col-xs-4")
    ut_categories = ut_day_passes[0].find_all(recursive=False)
    ut_offpeak = ut_day_passes[1].find_all(recursive=False)
    ut_peak = ut_day_passes[2].find_all(recursive=False)

    ut_categories_arr = ut_categories[0].find_all("h2")
    ut_offpeak_arr = ut_offpeak[0].find_all(["h2","h3"])
    ut_peak_arr = ut_peak[0].find_all(["h2","h3"])

    for i in range(len(ut_categories_arr)):
        ut_category = ut_categories_arr[i].text
        if ut_category in ignore_list:
            continue
        data.append({
            "key": "Camp5_ut_day_pass_offpeak",
            "category": ut_category,
            "price": ut_offpeak_arr[i].text.replace("MYR","RM")
        })
    for i in range(len(categories_arr)):
        ut_category = categories_arr[i].text
        if ut_category in ignore_list:
            continue
        data.append({
            "key": "Camp5_ut_day_pass_peak",
            "category": ut_category,
            "price": ut_peak_arr[i].text.replace("MYR","RM")
        })

    ut_xs6bulk = soup.select(".wpb_column.vc_column_container.vc_col-sm-6.vc_col-xs-6")

    ut_tenday_pass_categories = ut_xs6bulk[0].find_all(recursive=False)
    ut_tenday_pass_prices = ut_xs6bulk[1].find_all(recursive=False)
    ut_tenday_categories_arr = ut_tenday_pass_categories[0].find_all("h2")
    ut_tenday_prices_arr = ut_tenday_pass_prices[0].find_all("h3")

    for i in range(len(ut_tenday_categories_arr)):
        ut_tenday_category = ut_tenday_categories_arr[i].text
        if ut_tenday_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_ut_tenday_pass",
            "category": ut_tenday_category,
            "price": ut_tenday_prices_arr[i].text.replace("MYR","RM")   
        })

    ut_monthly_passes_categories = ut_xs6bulk[2].find_all(recursive=False)
    ut_monthly_pass_prices = ut_xs6bulk[3].find_all(recursive=False)
    ut_monthly_categories_arr = ut_monthly_passes_categories[0].find_all(["h2","h3"])
    ut_monthly_prices_arr = ut_monthly_pass_prices[0].find_all("h3")

    for i in range(len(ut_monthly_categories_arr)):
        ut_monthly_category = ut_monthly_categories_arr[i].text
        if ut_monthly_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_ut_monthly_pass",
            "category": ut_monthly_category,
            "price": ut_monthly_prices_arr[i].text.replace("MYR","RM")
        })

    ut_3month_passes_categories = ut_xs6bulk[8].find_all(recursive=False)
    ut_3month_pass_prices = ut_xs6bulk[9].find_all(recursive=False)
    ut_3month_categories_arr = ut_3month_passes_categories[0].find_all(["h2","h3"])
    ut_3month_prices_arr = ut_3month_pass_prices[0].find_all("h3")

    for i in range(len(ut_3month_categories_arr)):
        ut_3month_category = ut_3month_categories_arr[i].text
        if ut_3month_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_ut_3month_pass",
            "category": ut_3month_category,
            "price": ut_3month_prices_arr[i].text.replace("MYR","RM")
        })
    
    ut_year_passes_categories = ut_xs6bulk[12].find_all(recursive=False)
    ut_year_pass_prices = ut_xs6bulk[13].find_all(recursive=False)
    ut_year_categories_arr = ut_year_passes_categories[0].find_all(["h2","h3"])
    ut_year_prices_arr = ut_year_pass_prices[0].find_all("h3")

    for i in range(len(ut_year_categories_arr)):
        ut_year_category = ut_year_categories_arr[i].text
        if ut_year_category in ignore_list:
            continue

        data.append({
            "key": "Camp5_ut_year_pass",
            "category": ut_year_category,
            "price": ut_year_prices_arr[i].text.replace("MYR","RM")
        })

else:
    print(f'Failed to retrieve the webpage. Status code: {camp5_ut_response.status_code}')


batuu_pass_type_arr = ["bo","fg"]
if batuu_response.status_code == 200:
    soup = BeautifulSoup(batuu_response.text, 'html.parser')

    batuu_passes = soup.select(".grid.grid-cols-2.gap-2")

    offpeak_batuu_categories = batuu_passes[0].find_all("span")
    for i,offpeak_batuu_spans in enumerate(offpeak_batuu_categories):
        offpeak_batuu_price = offpeak_batuu_spans.find_parent("div")
        
        data.append({
            "key": "Batuu_offpeak_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": offpeak_batuu_price.text.replace("RM","RM ")
        })

    peak_batuu_categories = batuu_passes[1].find_all("span")
    for i,peak_batuu_spans in enumerate(peak_batuu_categories):
        peak_batuu_price = peak_batuu_spans.find_parent("div")

        data.append({
            "key": "Batuu_peak_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": peak_batuu_price.text.replace("RM","RM ")
        })

    batuu_10day_categories = batuu_passes[2].find_all("span")
    for i, batuu_10day_spans in enumerate(batuu_10day_categories):
        batuu_10day_price = batuu_10day_spans.find_parent("div")
        if "Upgrade" in batuu_10day_price.text: #Dumb website design
            continue
        data.append({
            "key": "Batuu_10day_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": batuu_10day_price.text.replace("RM","RM ")
        })

    batuu_monthly_categories = batuu_passes[3].find_all("span")
    for i, batuu_monthly_spans in enumerate(batuu_monthly_categories):
        batuu_monthly_price = batuu_monthly_spans.find_parent("div")
        if "Upgrade" in batuu_monthly_price.text: #Dumb website design
            continue
        data.append({
            "key": "Batuu_monthly_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": batuu_monthly_price.text.replace("RM","RM ")
        })

    batuu_6month_categories = batuu_passes[4].find_all("span")
    for i, batuu_6month_spans in enumerate(batuu_6month_categories):
        batuu_6month_price = batuu_6month_spans.find_parent("div")
        if "Upgrade" in batuu_6month_price.text: #Dumb website design
            continue
        data.append({
            "key": "Batuu_6month_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": batuu_6month_price.text.replace("RM","RM ")
        })
    
    batuu_year_categories = batuu_passes[5].find_all("span")
    for i, batuu_year_spans in enumerate(batuu_year_categories):
        batuu_year_price = batuu_year_spans.find_parent("div")
        if "Upgrade" in batuu_year_price.text: #Dumb website design
            continue
        data.append({
            "key": "Batuu_year_"+batuu_pass_type_arr[i],
            "category": "ADULT",
            "price": batuu_year_price.text.replace("RM","RM ")
        })
else:
    print(f'Failed to retrieve the webpage. Status code: {batuu_response.status_code}')

if bump_response.status_code == 200:
    soup = BeautifulSoup(bump_response.text, 'html.parser')

    bump_prices = soup.select(".font_4.wixui-rich-text__text")
   
    data.append({
            "key": "bump_daily_peak",
            "category": "ADULT",
            "price": bump_prices[0].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_daily_offpeak",
            "category": "ADULT",
            "price": bump_prices[1].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_10day",
            "category": "ADULT",
            "price": bump_prices[3].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_monthly",
            "category": "ADULT",
            "price": bump_prices[5].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_30day",
            "category": "ADULT",
            "price": bump_prices[6].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_6month",
            "category": "ADULT",
            "price": bump_prices[7].text.replace("RM","RM ")
        })
    data.append({
            "key": "bump_year",
            "category": "ADULT",
            "price": bump_prices[8].text.replace("RM","RM ")
        })
else:
    print(f'Failed to retrieve the webpage. Status code: {bump_response.status_code}')


if bhub_response.status_code == 200:
    soup = BeautifulSoup(bhub_response.text, 'html.parser')

    bhub_prices = soup.select(".elementor-heading-title.elementor-size-default")
    
    data.append({
            "key": "bhub_daily_peak",
            "category": "ADULT",
            "price": bhub_prices[2].text.replace("Peak hourRM","RM ").strip()
        })
    data.append({
            "key": "bhub_daily_offpeak",
            "category": "ADULT",
            "price": bhub_prices[3].text.replace("Off-Peak HourRM","RM ")
        })
    data.append({
            "key": "bhub_10day",
            "category": "ADULT",
            "price": bhub_prices[6].text
        })
    
    bhub_member_prices = soup.select(".elementor-element.elementor-element-cd506d9.e-con-full.e-flex.e-con.e-child")
    for bhmp in bhub_member_prices:
        bhub_m_price = bhmp.find_all("span")
        
        data.append({
            "key": "bhub_3m",
            "category": "ADULT",
            "price": bhub_m_price[0].text.replace("\n","").strip().replace("RM","RM ")
        })

        data.append({
            "key": "bhub_1m",
            "category": "ADULT",
            "price": bhub_m_price[4].text.replace("\n","").strip().replace("RM","RM ")
        })

        data.append({
            "key": "bhub_1y",
            "category": "ADULT",
            "price": bhub_m_price[9].text.replace("\n","").strip().replace(",","").replace("RM","RM ")
        })

        #Might do other smaller gyms next time(MadMonkeyz,BolderVentures,BoulderStory)

else:
    print(f'Failed to retrieve the webpage. Status code: {bhub_response.status_code}')


finaldata.append({
        "Type":"Weekday Offpeak/Peak",
        "Camp5 Single Gym": "10am-4pm/4pm-10pm",
        "Camp5 Multi Gym": "10am-4pm/4pm-10pm",
        "Camp5 Utropolis": "10am-4pm/4pm-10pm",
        "Batuu Boulder only": "10am-5pm/5pm-10pm",
        "Batuu Full gym": "10am-5pm/5pm-10pm",
        "Bump": "12pm-5pm/5pm-11pm",
        "Bhub": "11am-4pm,9pm-11pm/4pm-9pm"

    })

finaldata.append({
        "Type":"Daily Peak",
        "Camp5 Single Gym": data[1]["price"],
        "Camp5 Multi Gym": data[1]["price"],
        "Camp5 Utropolis": data[10]["price"],
        "Batuu Boulder only": data[17]["price"],
        "Batuu Full gym": data[18]["price"],
        "Bump": data[27]["price"],
        "Bhub": data[34]["price"]

    })
finaldata.append({
        "Type":"Daily Off Peak",
        "Camp5 Single Gym": data[0]["price"],
        "Camp5 Multi Gym": data[0]["price"],
        "Camp5 Utropolis": data[9]["price"],
        "Batuu Boulder only": data[15]["price"],
        "Batuu Full gym": data[16]["price"],
        "Bump": data[28]["price"],
        "Bhub": data[35]["price"]
    })
finaldata.append({
        "Type":"10 Day Pass",
        "Camp5 Single Gym": data[2]["price"],
        "Camp5 Multi Gym": data[2]["price"],
        "Camp5 Utropolis": data[11]["price"],
        "Batuu Boulder only": data[19]["price"],
        "Batuu Full gym": data[20]["price"],
        "Bump": data[29]["price"],
        "Bhub": data[36]["price"]
    })
finaldata.append({
        "Type":"Monthly Pass",
        "Camp5 Single Gym": data[3]["price"],
        "Camp5 Multi Gym": data[4]["price"],
        "Camp5 Utropolis": data[12]["price"],
        "Batuu Boulder only": data[21]["price"],
        "Batuu Full gym": data[22]["price"],
        "Bump": data[30]["price"],
        "Bhub": data[38]["price"]
    })
finaldata.append({
        "Type":"30 Day Pass",
        "Camp5 Single Gym": "-",
        "Camp5 Multi Gym": "-",
        "Camp5 Utropolis": "-",
        "Batuu Boulder only": "-",
        "Batuu Full gym": "-",
        "Bump": data[31]["price"],
        "Bhub": "-"
    })
finaldata.append({
        "Type":"3 Month Pass",
        "Camp5 Single Gym": data[5]["price"],
        "Camp5 Multi Gym": data[6]["price"],
        "Camp5 Utropolis": data[13]["price"],
        "Batuu Boulder only": "-",
        "Batuu Full gym": "-",
        "Bump": "-",
        "Bhub": data[37]["price"]
    })
finaldata.append({
        "Type":"6 Month Pass",
        "Camp5 Single Gym": "-",
        "Camp5 Multi Gym": "-",
        "Camp5 Utropolis": "-",
        "Batuu Boulder only": data[23]["price"],
        "Batuu Full gym": data[24]["price"],
        "Bump": data[32]["price"],
        "Bhub": "-"
    })
finaldata.append({
        "Type":"1 Year Pass",
        "Camp5 Single Gym": data[7]["price"],
        "Camp5 Multi Gym": data[8]["price"],
        "Camp5 Utropolis": data[14]["price"],
        "Batuu Boulder only": data[25]["price"],
        "Batuu Full gym": data[26]["price"],
        "Bump": data[33]["price"],
        "Bhub": data[39]["price"]
    })
# for x in data:
#     print(x["key"])
#     finaldata.append({
#         "Type":"Daily Peak"

#     })
    # print(x['key'])
print(json.dumps(finaldata))
# print(data)
# print(json.dumps(data))


# datat = open("scraper2result.txt", "r").read()
# modified_data = datat.replace("'", "\"")
# print(modified_data)
# print("THIS IS MODIFIED")
