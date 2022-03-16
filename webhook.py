import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import pandas as pd




url="https://oyoenterprise.webhook.office.com/webhookb2/ad40733b-2c8e-4d8a-833c-016e5d1d3030@04ec3963-dddc-45fb-afb7-85fa38e19b99/IncomingWebhook/65e3f90f975242ef87d4a6c28cca44d3/a3fa0b73-93cc-4cf0-945e-049bd89348e7"
title="Automated Notification about kubecost"
content = """
The content of this notification is <i>special</i>.<br>
It is the list of my favorite <b>fruits</b>
<ul>
<li>Lychee</li>
<li>Orange</li>
<li>Donuts</li>
</ul>
And also a demonstration of an HTML content used for a Teams notification<br>
😍
"""
# r = requests.get("https://kubecost.k8s2.oyorooms.io/allocations.html?window=24h&agg=deployment&chartDisplay=series&idle=hide&rate=daily&filters=W3sicHJvcGVydHkiOiJuYW1lc3BhY2UiLCJ2YWx1ZSI6Im93bmRlbCJ9XQ%3D%3D")
# print(r.text)
content1="""
 <table class="MuiTable-root"><thead class="MuiTableHead-root"><tr class="MuiTableRow-root MuiTableRow-head"><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignLeft" scope="col" style="width: 30px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false"><svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignLeft" scope="col" style="width: auto;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">Name<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">CPU<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">GPU<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">RAM<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">PV<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">Network<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">LB<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">Shared<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">External<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root" tabindex="0" role="button" aria-disabled="false">Efficiency<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionAsc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th><th class="MuiTableCell-root MuiTableCell-head MuiTableCell-alignRight" aria-sort="descending" scope="col" style="width: 90px;"><span class="MuiButtonBase-root MuiTableSortLabel-root MuiTableSortLabel-active" tabindex="0" role="button" aria-disabled="false">Total cost<svg class="MuiSvgIcon-root MuiTableSortLabel-icon MuiTableSortLabel-iconDirectionDesc" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></svg></span></th></tr></thead><tbody class="MuiTableBody-root"><tr class="MuiTableRow-root"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter" style="font-weight: 500;"></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft" style="font-weight: 500;">Totals</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$6.24</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$2.77</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.21</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">32.9%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight" style="font-weight: 500;">$9.22</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-smacs-api-2</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$1.99</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.30</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">15%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$2.32</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-smacs-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$1.24</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.57</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">50.5%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$1.84</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-partnerbff-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.76</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.62</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.02</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">31.6%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$1.40</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-storm-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.76</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.45</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.02</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">44.7%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$1.24</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-hits-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.48</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.21</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">30%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.72</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-storm-async-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.32</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.24</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.02</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">81.7%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.57</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-pcs-comm-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.19</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.16</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.02</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">27.8%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.37</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-spider-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.14</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.07</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">27.2%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.22</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-website-builder-web-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.12</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.05</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">47.9%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.18</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-pages-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.07</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">26.8%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.11</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-websitecms-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.07</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">36.4%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.10</td></tr><tr class="MuiTableRow-root" title="Cannot drill down"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-richie-api-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.07</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.02</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">33.7%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.10</td></tr><tr class="MuiTableRow-root"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft"><button class="MuiButtonBase-root MuiIconButton-root Mui-disabled Mui-disabled" tabindex="-1" type="button" disabled="" style="padding: 2px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft">prod-owndel-coyowebapp-web-1</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.03</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.01</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.00</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">56.6%</td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight">$0.05</td></tr></tbody></table>
  """

def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    # driver.get("https://kubecost.k8s2.oyorooms.io/allocations.html?window=24h&agg=deployment&chartDisplay=series&idle=hide&rate=daily&filters=W3sicHJvcGVydHkiOiJuYW1lc3BhY2UiLCJ2YWx1ZSI6Im93bmRlbCJ9XQ%3D%3D")
    # time.sleep(5)
    # wholeTable = driver.find_element_by_class_name("MuiTableContainer-root").get_attribute("innerHTML")
    # tableHeader = driver.find_element_by_class_name("MuiTableHead-root").get_attribute("innerHTML")
    # tableBody = driver.find_element_by_class_name("MuiTableBody-root").get_attribute("innerHTML")
    # soupTableHeader = BeautifulSoup(tableHeader,features="html.parser")
    # soupTableBody = BeautifulSoup(tableBody,features="html.parser")

    # costMatrix = []
    # heading = []
    # textInTableHeader = soupTableHeader.findAll('span')
    # for el in textInTableHeader:
    #     heading.append(el.text)
    #     # print(el.text)
    #     # html = el.get_attribute('innerHTML')
    #     # print(html)
    # # print(details)
    # costMatrix.append(heading)
    # # print(costMatrix)
    # # content=wholeTable
    # # print(len(soupTableBody))


    # for tb in soupTableBody:
    #     row = []
    #     # soupTableBodyRow = BeautifulSoup(tb,features="html.parser")
    #     textInTableBodyRow = tb.findAll('td')
    #     for td in textInTableBodyRow:
    #         row.append(td.text)
    #         # print(td.text)
    #     costMatrix.append(row)
    #     # print(tb)

    # # print(costMatrix)
    # for i in costMatrix:
    #     print(i)


    # df = pd.DataFrame(costMatrix[1:], columns=costMatrix[0])
    # print(df.to_html())


    # content = df.to_html()
    # MuiTable-root
    """
      - Send a teams notification to the desired webhook_url
      - Returns the status code of the HTTP request
        - webhook_url : the url you got from the teams webhook configuration
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": color,
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "activitySubtitle": content
            }],
        },
    )
    return response.status_code

# send_teams(url, content1, title)


def sendCostMatrixAlerts():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://kubecost.k8s2.oyorooms.io/allocations.html?window=24h&agg=deployment&chartDisplay=series&idle=hide&rate=daily&filters=W3sicHJvcGVydHkiOiJuYW1lc3BhY2UiLCJ2YWx1ZSI6Im93bmRlbCJ9XQ%3D%3D")
    time.sleep(5)
    wholeTable = driver.find_element_by_class_name("MuiTableContainer-root").get_attribute("innerHTML")
    tableHeader = driver.find_element_by_class_name("MuiTableHead-root").get_attribute("innerHTML")
    tableBody = driver.find_element_by_class_name("MuiTableBody-root").get_attribute("innerHTML")
    soupTableHeader = BeautifulSoup(tableHeader, features="html.parser")
    soupTableBody = BeautifulSoup(tableBody, features="html.parser")

    costMatrix = []
    heading = []
    textInTableHeader = soupTableHeader.findAll('span')
    for el in textInTableHeader:
        heading.append(el.text)
        # print(el.text)
        # html = el.get_attribute('innerHTML')
        # print(html)
    # print(details)
    costMatrix.append(heading)
    # print(costMatrix)
    # content=wholeTable
    # print(len(soupTableBody))


    for tb in soupTableBody:
        row = []
        # soupTableBodyRow = BeautifulSoup(tb,features="html.parser")
        textInTableBodyRow = tb.findAll('td')
        for td in textInTableBodyRow:
            row.append(td.text)
            # print(td.text)
        costMatrix.append(row)
        # print(tb)

    # print(costMatrix)
    # for i in costMatrix:
    #     print(i)


    
    # print(df.to_html())

    costMatrixOfUnderPerforming = []
    counter = 0;
    costMatrixOfUnderPerforming.append(costMatrix[0])



    for i in costMatrix:
        if counter >= 2:
            print(i[10])
            if i[10] < "30%":
                costMatrixOfUnderPerforming.append(i)
        counter=counter+1

    print(costMatrixOfUnderPerforming)




    df = pd.DataFrame(costMatrix[1:], columns=costMatrix[0])
    content = df.to_html()
    title = "Cost metrics of all service for past 24 hours"
    send_teams(url, content, title)

    df = pd.DataFrame(costMatrixOfUnderPerforming[1:], columns=costMatrixOfUnderPerforming[0])
    content = df.to_html()
    title = "Cost metrics of under utilised services for last 24 hours(Efficiency less than 30%)"
    send_teams(url, content, title)

sendCostMatrixAlerts()
