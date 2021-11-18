#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("13294333", 12345))
    API_HASH = os.environ.get("7cda3bc59ebc7161c00a356a05be5e6d")
    BOT_TOKEN = os.environ.get("2106830729:AAE9xX5bqiA9X4HuimtEKlUGBB11kpqcvLA", "") 
    BOT_SESSION = os.environ.get("AQDG6ZIGQvrhDuxTgWnDmyneqXFPW_sT5XbK-4uA4ncL1axNDs_1Dc8l61nigtJPwFpWR_kJOrGKCUDuAAZb9nVPjPfJPGdxYMGMjawAfQylyrkRa_ABhGgOwpcAB31mKIzoUS54cyfyrJQT475UoK48WRIQ16cqDRFwnpsaRPXVwbk7PmWWJJ4hk31WO_jOywHRNYYNUQ61oWk5b5qlNmWflArcAE7H_j3Hnv2ixmCFDYqZiRjzxJpKSefbhR_slYgy7cU6DObRY8RXdTMXvAez3qqfKpb-DjvllnA6U_l1Z7fakaDiVPi6zcqAOvmNDfdigMxQl8ujJX0cmXsbaC6WfX6QYwA", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("@mwkfiles", None)
    FILTER_TYPE = os.environ.get("empty", "")
    OWNER_ID = os.environ.get("2105446499", 12345)
    LIMIT = int(os.environ.get("0", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("AQDG6ZIGQvrhDuxTgWnDmyneqXFPW_sT5XbK-4uA4ncL1axNDs_1Dc8l61nigtJPwFpWR_kJOrGKCUDuAAZb9nVPjPfJPGdxYMGMjawAfQylyrkRa_ABhGgOwpcAB31mKIzoUS54cyfyrJQT475UoK48WRIQ16cqDRFwnpsaRPXVwbk7PmWWJJ4hk31WO_jOywHRNYYNUQ61oWk5b5qlNmWflArcAE7H_j3Hnv2ixmCFDYqZiRjzxJpKSefbhR_slYgy7cU6DObRY8RXdTMXvAez3qqfKpb-DjvllnA6U_l1Z7fakaDiVPi6zcqAOvmNDfdigMxQl8ujJX0cmXsbaC6WfX6QYwA")
    TO_CHANNEL = int(os.environ.get("-1001760095750", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
