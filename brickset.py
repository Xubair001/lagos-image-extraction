import requests

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=0, i",
    "referer": "https://brickset.com/minifigs?query=gen060",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"134.0.6998.88"',
    "sec-ch-ua-full-version-list": '"Chromium";v="134.0.6998.88", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.88"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.11.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    # 'cookie': 'ASP.NET_SessionId=qwspwxtufmo0xxupzkmp3szr; ActualCountry=CountryCode=US&CountryName=United States; PreferredCountry2=CountryCode=US&CountryName=United States; usprivacy=1---; _ga=GA1.1.322644465.1744812444; ad_clicker=false; _sharedid=4bb05d1e-bc3c-4e0b-9f59-8564d8f18e54; _li_dcdm_c=.brickset.com; _lc2_fpi=93114e3db128--01jrzet4e2gqp3wn8mgykewd7a; _lc2_fpi_meta=%7B%22w%22%3A1744812446147%7D; _lr_retry_request=true; _lr_env_src_ats=false; GN_USER_ID_KEY=9f28bcbe-04f6-49ef-8b9a-64005af1ede6; GN_SESSION_ID_KEY=327ecf91-98d5-432b-9702-69e31775e42e; panoramaId_expiry=1744898847624; _cc_id=b92fd01c10134006b93be2da357503fa; fpestid=b-qFUn32qKnnTn9QwbatM_Zd8Mm7Mj1MlT3BDPevwwzeFabrAAuZjIE6CKoB7_QgoGG3uA; _lr_sampling_rate=100; _lr_geo_location=US; _lr_geo_location_state=WA; darkmode=on; _au_1d=AU1D-0100-001744812514-03YCQ4JC-RT5W; bounceClientVisit8144v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgEYBOAlgMYDWKApggHSUD2AtkRAIakLob4AjgFc6pAJ6YAIgHM6AOwAMANkUgANCFIwQZKrQbN2GkCgRcEdGKAAmdAG5U6AfXI2dygIyKMADgCcPgAsyrj+qn7KGBgmMjYQ2tAAZlxg9JqUXChgMClpdJrCKDAIpKKado6UVtCgZCwA7vSJIADCcKTsVpr2YijkLPI6nhhBjIrj4yYQYBZJLKRsOgAy5PLCAB4mlU7OCOIQNSB2KNQILFCaZFzy7rAmDXTEjnQNuan0AL6a8izO1Gs6P1itBSuUtHQRECEHsWNQFDpFHRfGEMHR-H4AOyKGy+XyKRRJTHKOhcXw2Gy4JKUcneYhcLgqFKYoJJOhJDlsgCsXAwXK8-l8XEyYSSvi5JjYLGI5DANTy6RAjigsE8QX8jCCE1CjFwsToLGsIFYwnkpXEOgAqgBlEwAL3IKpAgs8qmmLDMqWcrDsOhdboy5H2OmtpKQcpMrDNgLN3pYvtgADksCZSHQZAMhrAAOopzRpjODZzyLhsI7ZrJwNYyc5DDIsU3m4ulo6W+RBug2AAE1vMlmK9cbEjjCZANsjDbNw59dBisBteZAPFJI6O2zYXFXMF8nn8mjLpT+M+3u80swQQeECaCmMYyjPgwzCCvNQAtJ5cLhGBhviAWBynHefJNBQFAknsBAYEUTQECzTwWSCHdcC5IIMBguEFAANXIfoEAASTuEB4KCRCPxQoIuRQxRUO2BwnDwqQPG8PxAlGUJwh8XwohiHocKDBjhgQpDyMorUaM+T4gA; _pubcid=f8179df3-517a-4b01-b7ba-84620020eceb; _pubcid_cst=VyxHLMwsHQ%3D%3D; pbjs-unifiedid=%7B%22TDID%22%3A%2274201a7a-1b0c-4366-b433-bd44a956590e%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222025-03-16T14%3A09%3A10%22%7D; pbjs-unifiedid_cst=VyxHLMwsHQ%3D%3D; __gads=ID=9477c9c067124f87:T=1744812452:RT=1744813544:S=ALNI_MbVUvM2OmZPXEhmW2TfnAjbiavPnw; __gpi=UID=0000109467ddacdf:T=1744812452:RT=1744813544:S=ALNI_MZzMHBKdpULhB_rpzwng6MV5zP2UQ; __eoi=ID=9e6613ef2cdbf43c:T=1744812452:RT=1744813544:S=AA-AfjZ0m04EF-_B0sYD75OSDl80; _ga_FVWZ0RM4DH=GS1.1.1744813564.1.0.1744813564.60.0.0; _ga_ZSNG05RX84=GS1.1.1744812443.1.1.1744813573.0.0.0; _awl=2.1744813583.5-0004ebc3e1e8baba08f51856c28383ca-6763652d75732d7765737431-0; _sharedid_cst=VyxHLMwsHQ%3D%3D; cto_bidid=t4OWHF9ya1RSbnlOdElzMHVqSUNOaUZwZTNxWURuRHpaZ1h6THpVVmpLJTJGVXFvJTJCejhMeEw0MWZObzE4clFRSFg2UCUyRktGNU1rVWVCRXRvZDZOdEFaYVRlaGM4NFZ4aHUxUHlHTTRXNWc4SzQwRVBLOCUzRA; cf_clearance=cWR7i8RxoGFl0D1D.L4zFB8KPL02H1C7ynxfnW5t.os-1744813616-1.2.1.1-tUHON4LBu_n6ELvbV9F9yhKACAMma2MzQX22Sdb1g2vD7tAU85IV.loC_4S2jDiVP_u7_D6_6.5qi3AWEuhpmYjRSorqpCpZ52r9vNxXRRHiOl_rb39KEOqlRsyAJpjAyRO3oxdJ10Y5e_q3bGxjDHW0fn66cXTF4pyIivu9tl.ozWmkXRc8EneVaXe0kjzYqZqd5sOOET0LDF4RbWpfE9cZmX12UsC3_G48z0OGTJCEFCfUC0ejr3tzRjUYuPKKSFKCP43NwivsQ2s9UNjN69Tn5J6iAQ_GbLGMJf.qGOheyJ1FJrVMPaMnecLeKjlFSNK9tezdozOW8M6aK.2Syaj.A6f1aEH7EqFqqIjRkgI; cto_bundle=7salUV9VOHA2ZFRCUXE3clhVbGJ2bGQ3UHFORjZkZWpUJTJCTGV6OVZvQkU0Qng0cHlZSDA3aGJJTHBCdWV4cFdlZWVLVjN2ZTd0S01vJTJCSnR3S3NRbzNaclB5JTJGNzA1Y0tlUVdRdGwxdERnakJUZmZtbUtLeDlBRVUyRkpWUkJPdVEwaG1mWEZjRWlqJTJCcW1uUE5JcERHRHlKOHJLRFJOUFFMaTBFTU1TVzQ1V1FwSGNiOCUzRA; _ga_EFZWYSQ4VF=GS1.1.1744812446.1.1.1744813688.0.0.0',
}

params = {
    "query": "gen060",
    "scope": "All",
}

response = requests.get(
    "https://brickset.com/search", params=params, headers=headers, timeout=10
)
