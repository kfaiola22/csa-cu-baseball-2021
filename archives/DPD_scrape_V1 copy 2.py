# web scraping script attempt 1
# DP Dough Zone of the Day Calendar
# March 9, 2020

from bs4 import BeautifulSoup
import requests

# import csv
# csv_file = open('DPDough_Scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['title', 'subtitle', 'days of the week', 'first week', 'second week', 'third week', 'fourth week', 'day number', 'zotd' ])
#
#
# for zotds in soup.findall():

source = requests.get('https://www.dpdough.com/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

body = soup.find('body')
# print(body.prettify())

contains = body.find('div', id='container')
homepage = contains.find('div', id='homepage')
calzoneotd = homepage.find('div', class_='home-zoneoftheday')
#print(calzoneotd)
zotd_calendar = calzoneotd.find('div', class_='home-zoneofthedaycalendar-link')
#print(zotd_calendar)
zotd_cal_link = zotd_calendar.a.get('href')
print(zotd_cal_link)

new_source = requests.get('zotd_cal_link').text
more_soup = BeautifulSoup(new_source, 'lxml')
new_body = more_soup.find('body')
container = new_body.find('div', id='container')
calendar = container.find('div', class_= 'zoneoftheday-calendar')
title_zotd = calendar.find('div', class_='zoneoftheday-calendar-title')
subtitle_month = calendar.find('div',class_='zoneoftheday-calendar-subtitle')
daysofweek = calendar.find('div', class_='zoneoftheday-calendar-week names')
for days in daysofweek:
    day_name[days] = daysofweek.find('div', class_='zoneoftheday-calendar-week-day'))
for week in range(0,3):
    week =
#check out findall to grab particular tags with specific classes - one line




# csv_file.close()






#find('a', class_='button-zoneoftheday')
#print(zotd_cal_lk)


# zone of the day calendar link section line
#<a class="button-zoneoftheday" href="https://www.dpdough.com/zone-of-the-day-calendar/"></a>

# Zone of the day calendar section header
#<div class="home-zoneofthedaycalendar-link"><a class="button-zoneoftheday" href="https://www.dpdough.com/zone-of-the-day-calendar/"></a></div>

#CALZONE OF THE DAY SECTION
# <div class="home-zoneoftheday">
# <div class="bg-element zoneoftheday" data-url="https://www.dpdough.com/wp-admin/admin-ajax.php"></div><div class="home-zoneoftheday-rotator"><div class="home-zoneoftheday-rotator-slide" style="cursor: pointer;"><a onclick="addToOloCart(117)"><img alt="Drop Zone" src="https://dpdough.com/wp-content/uploads/2018/07/ZOTD_DropZone.jpg"/></a></div></div>
# <div class="home-zoneoftheday-week">
# <div class="home-zoneoftheday-week-today">
# <div class="home-zoneoftheday-week-day-date"><strong>Today</strong><span>Mar 9</span><div class="zotd-line-left"><img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/></div></div>
# <div class="home-zoneoftheday-week-today-zone">Drop Zone<div class="home-zoneoftheday-week-day-description">Breaded Chicken, Pepperoni, Mozzarella, Parmesan, Ricotta</div></div>
# </div><div class="home-zoneoftheday-week-day">
# <div class="home-zoneoftheday-week-day-date"><strong>Tue</strong><span>Mar 10</span><div class="zotd-line-right"><img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/></div></div>
# <div class="home-zoneoftheday-week-day-zone">Italian Zone</div>
# </div><div class="home-zoneoftheday-week-day">
# <div class="home-zoneoftheday-week-day-date"><strong>Wed</strong><span>Mar 11</span><div class="zotd-line-right"><img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/></div></div>
# <div class="home-zoneoftheday-week-day-zone">2 For #Winsday</div>
# </div><div class="home-zoneoftheday-week-day">
# <div class="home-zoneoftheday-week-day-date"><strong>Thu</strong><span>Mar 12</span><div class="zotd-line-right"><img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/></div></div>
# <div class="home-zoneoftheday-week-day-zone">Speed Zone</div>
# </div>
# </div>
# <div class="home-zoneofthedaycalendar-link"><a class="button-zoneoftheday" href="https://www.dpdough.com/zone-of-the-day-calendar/"></a></div>
# </div>
#FULL SOURCE:
# !DOCTYPE html>
# <html lang="en-US">
#  <head>
#   <!-- Google Tag Manager -->
#   <script>
#    (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-M6M2T6X');
#   </script>
#   <!-- End Google Tag Manager -->
#   <title>
#    Home - D.P. Dough
#   </title>
#   <meta content="The Original Calzone Company" name="description"/>
#   <meta charset="utf-8"/>
#   <meta content="width=device-width, initial-scale=1" name="viewport"/>
#   <link href="http://gmpg.org/xfn/11" rel="profile"/>
#   <!-- This site is optimized with the Yoast SEO plugin v11.8 - https://yoast.com/wordpress/plugins/seo/ -->
#   <link href="https://www.dpdough.com/" rel="canonical"/>
#   <meta content="en_US" property="og:locale"/>
#   <meta content="website" property="og:type"/>
#   <meta content="Home - D.P. Dough" property="og:title"/>
#   <meta content="https://www.dpdough.com/" property="og:url"/>
#   <meta content="D.P. Dough" property="og:site_name"/>
#   <meta content="summary" name="twitter:card"/>
#   <meta content="Home - D.P. Dough" name="twitter:title"/>
#   <script class="yoast-schema-graph yoast-schema-graph--main" type="application/ld+json">
#    {"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://www.dpdough.com/#website","url":"https://www.dpdough.com/","name":"D.P. Dough","potentialAction":{"@type":"SearchAction","target":"https://www.dpdough.com/?s={search_term_string}","query-input":"required name=search_term_string"}},{"@type":"WebPage","@id":"https://www.dpdough.com/#webpage","url":"https://www.dpdough.com/","inLanguage":"en-US","name":"Home - D.P. Dough","isPartOf":{"@id":"https://www.dpdough.com/#website"},"datePublished":"2014-04-04T21:26:15-04:00","dateModified":"2018-07-02T13:43:21-04:00"}]}
#   </script>
#   <!-- / Yoast SEO plugin. -->
#   <link href="//s.w.org" rel="dns-prefetch"/>
#   <script type="text/javascript">
#    window._wpemojiSettings={"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.dpdough.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.2.5"}};!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline="top",l.font="600 32px Arial",a){case"flag":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]),!b);case"emoji":return b=d([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340]),!b}return!1}function f(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var g,h,i,j,k=b.createElement("canvas"),l=k.getContext&&k.getContext("2d");for(j=Array("flag","emoji"),c.supports={everything:!0,everythingExceptFlag:!0},i=0;i<j.length;i++)c.supports[j[i]]=e(j[i]),c.supports.everything=c.supports.everything&&c.supports[j[i]],"flag"!==j[i]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[j[i]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(h=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",h,!1),a.addEventListener("load",h,!1)):(a.attachEvent("onload",h),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),g=c.source||{},g.concatemoji?f(g.concatemoji):g.wpemoji&&g.twemoji&&(f(g.twemoji),f(g.wpemoji)))}(window,document,window._wpemojiSettings);
#   </script>
#   <style type="text/css">
#    img.wp-smiley,img.emoji{display:inline!important;border:none!important;box-shadow:none!important;height:1em!important;width:1em!important;margin:0 .07em!important;vertical-align:-.1em!important;background:none!important;padding:0!important}
#   </style>
#   <link href="https://www.dpdough.com/wp-content/plugins/formidable/css/formidableforms.css?ver=811209" id="formidable-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/plugins/ultimate-responsive-image-slider-pro/fancybox/jquery.fancybox.css?ver=5.2.5" id="risp-fancybox-css-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/plugins/ultimate-responsive-image-slider-pro/css/risp.css?ver=5.2.5" id="risp-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/plugins/ultimate-responsive-image-slider-pro/css/slider-pro.min.css?ver=5.2.5" id="risp-slider-pro-min-css-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-includes/css/dist/block-library/style.min.css?ver=5.2.5" id="wp-block-library-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/plugins/pdf-embedder/css/pdfemb-blocks.css?ver=5.2.5" id="pdfemb-gutenberg-block-backend-js-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/css/chalkboard.css?ver=5.2.5" id="chalkboard-style-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/css/mobile.css?ver=5.2.5" id="chalkboard-mobile-style-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/css/default.css?ver=5.2.5" id="chalkboard-banners-default-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/css/nivo-slider.css?ver=5.2.5" id="chalkboard-banners-style-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-content/plugins/login-api-wp/css/style.css?ver=1583731516" id="style-css-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://www.dpdough.com/wp-json/" rel="https://api.w.org/"/>
#   <link href="https://www.dpdough.com/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
#   <link href="https://www.dpdough.com/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
#   <meta content="WordPress 5.2.5" name="generator"/>
#   <link href="https://www.dpdough.com/" rel="shortlink"/>
#   <link href="https://www.dpdough.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.dpdough.com%2F" rel="alternate" type="application/json+oembed"/>
#   <link href="https://www.dpdough.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.dpdough.com%2F&amp;format=xml" rel="alternate" type="text/xml+oembed"/>
#   <script type="text/javascript">
#    document.documentElement.className+=" js";
#   </script>
#   <script src="https://www.google.com/recaptcha/api.js">
#   </script>
#   <!-- Facebook Pixel Code -->
#   <script>
#    !function(f,b,e,v,n,t,s)
# {if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','2312682335411149');fbq('track','PageView');
#   </script>
#   <noscript>
#    <img height="1" src="https://www.facebook.com/tr?id=2312682335411149&amp;ev=PageView&amp;noscript=1" width="1"/>
#   </noscript>
#   <!-- End Facebook Pixel Code -->
#  </head>
#  <body class="home page-template page-template-chalkboard-homepage page-template-chalkboard-homepage-php page page-id-18">
#   <!-- Google Tag Manager (noscript) -->
#   <noscript>
#    <iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-M6M2T6X" style="display:none;visibility:hidden" width="0">
#    </iframe>
#   </noscript>
#   <!-- End Google Tag Manager (noscript) -->
#   <div class="side-socials">
#    <a href="https://twitter.com/dpdough" target="_blank">
#     <i class="fa fa-twitter">
#     </i>
#    </a>
#    <a href="https://www.instagram.com/dpdough/" target="_blank">
#     <i class="fa fa-instagram">
#     </i>
#    </a>
#    <a href="https://www.facebook.com/dpdoughcalzones/" target="_blank">
#     <i class="fa fa-facebook">
#     </i>
#    </a>
#    <a href="https://www.youtube.com/channel/UC8EgLtr6-1JsNi24lihc0zA" target="_blank">
#     <i class="fa fa-youtube">
#     </i>
#    </a>
#   </div>
#   <div class="secondary" id="menu">
#    <div id="logo">
#     <a href="/">
#      <img alt="D.P. Dough" class="logo_menu" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/logo_dpdough.png"/>
#     </a>
#    </div>
#    <div id="menu_header">
#     <div class="menu-header-order-online" id="menu_olo_link">
#      <a href="/locations">
#       <img alt="Order Online" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/button_orderonline.png"/>
#      </a>
#     </div>
#     <div class="menu-header-submenu">
#      <ul class="nav navbar-nav" id="menu-chalkboard-header">
#       <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2818" id="menu-item-2818">
#        <a href="https://www.dpdough.com/menu/">
#         Menu
#        </a>
#       </li>
#       <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2819" id="menu-item-2819">
#        <a href="https://www.dpdough.com/locations/">
#         Locations
#        </a>
#       </li>
#       <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2822" id="menu-item-2822">
#        <a href="https://www.dpdough.com/job-application/">
#         Jobs
#        </a>
#       </li>
#       <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5969" id="menu-item-5969">
#        <a href="https://dpdough.fancollab.com/" rel="noopener noreferrer" target="_blank">
#         Merch
#        </a>
#       </li>
#       <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2820" id="menu-item-2820">
#        <a href="https://www.dpdough.com/contact-us/">
#         Contact Us
#        </a>
#       </li>
#      </ul>
#     </div>
#    </div>
#    <div id="menu_bg">
#    </div>
#   </div>
#   <div id="olo_fixed">
#    <a class="order-online-store-link" href="" id="olo_fixed_link">
#     <img alt="Order Online" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/button_orderonline_mobile.png"/>
#    </a>
#   </div>
#   <div id="container">
#    <div id="homepage">
#     <div id="wrapper">
#      <div class="slider-wrapper theme-default">
#       <div class="nivoSlider" id="slider">
#        <a href="/locations">
#         <img alt="" data-thumb="https://dpdough.com/wp-content/uploads/2020/01/RotatorMacalo.jpg" src="https://dpdough.com/wp-content/uploads/2020/01/RotatorMacalo.jpg"/>
#        </a>
#        <a href="/locations">
#         <img alt="" data-thumb="https://dpdough.com/wp-content/uploads/2019/08/OrderOnline_1200.jpg" src="https://dpdough.com/wp-content/uploads/2019/08/OrderOnline_1200.jpg"/>
#        </a>
#        <a href="/locations">
#         <img alt="" data-thumb="https://dpdough.com/wp-content/uploads/2019/10/OpenCrazyLateBatSignal.jpg" src="https://dpdough.com/wp-content/uploads/2019/10/OpenCrazyLateBatSignal.jpg"/>
#        </a>
#        <a href="/stoneycalzoney ">
#         <img alt="" data-thumb="https://dpdough.com/wp-content/uploads/2019/09/DPDough_Stoney.jpg" src="https://dpdough.com/wp-content/uploads/2019/09/DPDough_Stoney.jpg"/>
#        </a>
#       </div>
#      </div>
#     </div>
#     <div class="home-title wisacalzone">
#      <div class="home-title-name">
#       <div class="home-title-name-sup-text">
#        What Is A
#       </div>
#       Calzone
#       <span>
#        ?
#       </span>
#       <div class="line-right">
#        <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#       </div>
#      </div>
#     </div>
#     <div class="home-wisacalzone">
#      <div class="home-wisacalzone-pronunciation">
#       /kalˈzōnē,ˌkalˈtsōnā,ˌkalˈzōn/
#      </div>
#      <div class="home-wisacalzone-define">
#       a type of
#       <span class="strikethru">
#        pizza
#        <span class="strikethru-alternative">
#         ^awesome
#        </span>
#       </span>
#       made with your favorite ingredients and our original-recipe dough, folded, and fresh baked to order.
#      </div>
#      <div class="home-wisacalzone-calzone">
#       <div class="home-wisacalzone-calzone-image">
#        <img alt="D.P. Dough Calzone" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/graphic_calzone_open.png"/>
#        <div class="home-wisacalzone-calzone-ingredients">
#         <div class="home-wisacalzone-calzone-ingredients-arrowup">
#          <img src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/arrow_up_right.png"/>
#         </div>
#         Choose from 30+ ingredients
#        </div>
#        <div class="home-wisacalzone-calzone-dough">
#         <div class="home-wisacalzone-calzone-dough-arrowleft">
#          <img src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/arrow_down_left.png"/>
#         </div>
#         With our original recipe dough
#        </div>
#        <div class="home-wisacalzone-calzone-fresh-baked">
#         <div class="home-wisacalzone-calzone-fresh-baked-arrowupleft">
#          <img src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/arrow_up_left.png"/>
#         </div>
#         Fresh baked
#        </div>
#        <div class="home-wisacalzone-calzone-sauce">
#         <div class="home-wisacalzone-calzone-sauce-image">
#          <img src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/graphic_calzone_sauce.png"/>
#         </div>
#         <div class="home-wisacalzone-calzone-sauce-served">
#          Served with our signature marinara sauce
#          <div class="home-wisacalzone-calzone-sauce-served-arrowdownright">
#           <img src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/arrow_down_right.png"/>
#          </div>
#         </div>
#        </div>
#       </div>
#      </div>
#     </div>
#     <div class="home-title calzone">
#      <div class="home-title-name">
#       <div class="home-title-logo">
#        <img alt="D.P. Dough Calzone" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/icon_calzone.png"/>
#       </div>
#       Zone Of The Day
#       <div class="line-right">
#        <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#       </div>
#      </div>
#     </div>
#     <div class="zoneoftheday-calendar-desc">
#      Participating Locations Only
#     </div>
#     <div class="home-zoneoftheday">
#      <div class="bg-element zoneoftheday" data-url="https://www.dpdough.com/wp-admin/admin-ajax.php">
#      </div>
#      <div class="home-zoneoftheday-rotator">
#       <div class="home-zoneoftheday-rotator-slide" style="cursor: pointer;">
#        <a onclick="addToOloCart(116)">
#         <img alt="Danger Zone" src="https://dpdough.com/wp-content/uploads/2018/07/ZOTD_DangerZone.jpg"/>
#        </a>
#       </div>
#      </div>
#      <div class="home-zoneoftheday-week">
#       <div class="home-zoneoftheday-week-today">
#        <div class="home-zoneoftheday-week-day-date">
#         <strong>
#          Today
#         </strong>
#         <span>
#          Mar 8
#         </span>
#         <div class="zotd-line-left">
#          <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#        <div class="home-zoneoftheday-week-today-zone">
#         Danger Zone
#         <div class="home-zoneoftheday-week-day-description">
#          Hamburger, Cheddar, Onions, Hot Sauce, Taco Seasoning
#         </div>
#        </div>
#       </div>
#       <div class="home-zoneoftheday-week-day">
#        <div class="home-zoneoftheday-week-day-date">
#         <strong>
#          Mon
#         </strong>
#         <span>
#          Mar 9
#         </span>
#         <div class="zotd-line-right">
#          <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#        <div class="home-zoneoftheday-week-day-zone">
#         Drop Zone
#        </div>
#       </div>
#       <div class="home-zoneoftheday-week-day">
#        <div class="home-zoneoftheday-week-day-date">
#         <strong>
#          Tue
#         </strong>
#         <span>
#          Mar 10
#         </span>
#         <div class="zotd-line-right">
#          <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#        <div class="home-zoneoftheday-week-day-zone">
#         Italian Zone
#        </div>
#       </div>
#       <div class="home-zoneoftheday-week-day">
#        <div class="home-zoneoftheday-week-day-date">
#         <strong>
#          Wed
#         </strong>
#         <span>
#          Mar 11
#         </span>
#         <div class="zotd-line-right">
#          <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#        <div class="home-zoneoftheday-week-day-zone">
#         2 For #Winsday
#        </div>
#       </div>
#      </div>
#      <div class="home-zoneofthedaycalendar-link">
#       <a class="button-zoneoftheday" href="https://www.dpdough.com/zone-of-the-day-calendar/">
#       </a>
#      </div>
#     </div>
#     <div class="home-socials">
#      <div class="home-twitter">
#       <div class="bg-element socials" data-url="https://www.dpdough.com/wp-admin/admin-ajax.php">
#       </div>
#       <div class="home-title twitter">
#        <div class="home-title-name">
#         <div class="home-title-logo">
#          <img alt="@dpdough Twitter" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/icon_twitter.png"/>
#         </div>
#         Twitter
#         <div class="line-right">
#          <img alt="Home" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#       </div>
#       <div id="twitter-widget">
#        <a class="twitter-timeline" data-lang="en" data-link-color="#db0004" data-theme="dark" data-tweet-limit="3" href="https://twitter.com/dpdough?ref_src=twsrc%5Etfw">
#        </a>
#        <script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js">
#        </script>
#       </div>
#      </div>
#      <div class="home-instagram">
#       <div class="home-title instagram">
#        <div class="home-title-name">
#         <div class="home-title-logo">
#          <img alt="@dpdough Instagram" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/icon_instagram.png"/>
#         </div>
#         Instagram
#         <div class="line-right">
#          <img alt="Home" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#         </div>
#        </div>
#       </div>
#       <div id="instagram-widget">
#        <script src="https://snapwidget.com/js/snapwidget.js">
#        </script>
#        <iframe allowtransparency="true" class="snapwidget-widget" frameborder="0" scrolling="no" src="https://snapwidget.com/embed/533201" style="border:none; overflow:hidden; width:100%; ">
#        </iframe>
#       </div>
#      </div>
#     </div>
#     <div class="home-title merch">
#      <div class="home-title-name">
#       <div class="home-title-logo">
#        <img alt="D.P. Dough Merch" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/icon_merch.png"/>
#       </div>
#       Fresh Baked Merch
#       <div class="line-right">
#        <img alt="D.P. Dough" src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/img/bg_chalkline_red.png"/>
#       </div>
#      </div>
#     </div>
#     <div class="home-merch">
#      <div class="bg-element merch" data-url="https://www.dpdough.com/wp-admin/admin-ajax.php">
#      </div>
#      <div class="home-merch-item">
#       <div class="home-merch-item-photo">
#        <a href="https://dpdough.fancollab.com/teezone/vintage-logo-tee" target="_blank">
#         <img alt="Vintage Logo Tee" src="https://dpdough.com/wp-content/uploads/2018/04/merch_vintagedpdoughtee.jpg"/>
#        </a>
#       </div>
#       <div class="home-merch-item-title">
#        <a href="https://dpdough.fancollab.com/teezone/vintage-logo-tee" target="_blank">
#         Vintage Logo Tee
#        </a>
#       </div>
#      </div>
#      <div class="home-merch-item">
#       <div class="home-merch-item-photo">
#        <a href="https://dpdough.fancollab.com/teezone/fresh-baked-tee" target="_blank">
#         <img alt="Fresh Baked Tee" src="https://dpdough.com/wp-content/uploads/2018/04/merch_stoneycalzoneytee.jpg"/>
#        </a>
#       </div>
#       <div class="home-merch-item-title">
#        <a href="https://dpdough.fancollab.com/teezone/fresh-baked-tee" target="_blank">
#         Fresh Baked Tee
#        </a>
#       </div>
#      </div>
#      <div class="home-merch-item">
#       <div class="home-merch-item-photo">
#        <a href="https://dpdough.fancollab.com/teezone/i-heart-dp-dough-tee" target="_blank">
#         <img alt="I Heart D.P. Dough Tee" src="https://dpdough.com/wp-content/uploads/2019/01/DPDough_IHeart_Tee.jpg"/>
#        </a>
#       </div>
#       <div class="home-merch-item-title">
#        <a href="https://dpdough.fancollab.com/teezone/i-heart-dp-dough-tee" target="_blank">
#         I Heart D.P. Dough Tee
#        </a>
#       </div>
#      </div>
#     </div>
#     <div class="home-merch-link">
#      <a class="button-buynow" href="https://dpdough.fancollab.com/">
#      </a>
#     </div>
#    </div>
#   </div>
#   <footer class="home-footer">
#    <ul class="footer-links" id="menu-chalkboard-footer">
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2825" id="menu-item-2825">
#      <a href="https://www.dpdough.com/about-us/">
#       About D.P. Dough
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2833" id="menu-item-2833">
#      <a href="https://www.dpdough.com/contact-us/">
#       Contact Us
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2827" id="menu-item-2827">
#      <a href="https://www.dpdough.com/job-application/">
#       Jobs
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2828" id="menu-item-2828">
#      <a href="http://dpdough.papyrs.com/" rel="noopener noreferrer" target="_blank">
#       Owner’s Site
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2829" id="menu-item-2829">
#      <a href="https://www.dpdough.com/terms-and-conditions/">
#       Legal Stuff
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2836" id="menu-item-2836">
#      <a href="https://www.dpdough.com/fundraising/">
#       Fundraising
#      </a>
#     </li>
#     <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2837" id="menu-item-2837">
#      <a href="https://www.dpdough.com/nutritional-info/">
#       Nutritional Info
#      </a>
#     </li>
#    </ul>
#    <div id="ownadpdough">
#     <a class="button-ownadpdough" href="http://ownadpdough.com" target="_blank">
#     </a>
#    </div>
#    <div class="footer-copyright">
#     &amp;copy 2020 Copyright D.P. Dough Franchising, LLC.
#    </div>
#    <!-- Google Analytics & Ad Services -->
#    <script type="text/javascript">
#     //<![CDATA[
# var google_conversion_id=965781746;var google_custom_params=window.google_tag_params;var google_remarketing_only=true;
# //]]>
#    </script>
#    <script src="//www.googleadservices.com/pagead/conversion.js" type="text/javascript">
#    </script>
#    <noscript>
#     <div style="display:inline;">
#      <img alt="" height="1" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/965781746/?guid=ON&amp;script=0" style="border-style:none;" width="1"/>
#     </div>
#    </noscript>
#    <!-- // -->
#   </footer>
#   <script src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/js/jquery-1.12.4.min.js?ver=1.12.4" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/plugins/ultimate-responsive-image-slider-pro/js/jquery.sliderPro.min.js?ver=5.2.5" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/plugins/ultimate-responsive-image-slider-pro/fancybox/jquery.fancybox.pack.js?ver=5.2.5" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/plugins/login-api-wp/js/general.js?ver=1" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/plugins/login-api-wp/js/bootstrap.min.js?ver=3.3.7" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/js/jquery-ui.min.js?ver=1.11.4" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/js/jquery.mobile.custom.min.js?ver=1.4.5" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/js/jquery.nivo.slider.js?ver=3.2" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-includes/js/jquery/ui/core.min.js?ver=1.11.4" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-includes/js/jquery/ui/datepicker.min.js?ver=1.11.4" type="text/javascript">
#   </script>
#   <script type="text/javascript">
#    jQuery(document).ready(function(jQuery){jQuery.datepicker.setDefaults({"closeText":"Close","currentText":"Today","monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Previous","dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"dateFormat":"MM d, yy","firstDay":1,"isRTL":false});});
#   </script>
#   <script src="https://www.dpdough.com/wp-content/themes/dpdough-chalkboard/js/chalkboard.actions.js?ver=1.1.3" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-content/plugins/login-api-wp/js/services.js?ver=1583731516" type="text/javascript">
#   </script>
#   <script src="https://www.dpdough.com/wp-includes/js/wp-embed.min.js?ver=5.2.5" type="text/javascript">
#   </script>
#  </body>
# </html>
# >>>
