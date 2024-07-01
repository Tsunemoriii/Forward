import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "25697264"))
    API_HASH = os.environ.get("API_HASH", "fc1bce8441f3c90b719bc86098137a3d")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7360043493:AAESptsDLQskNMaJfedW2pD-YPk83-tVKnU")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1921693263")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://utahakane008:utahakane008@cluster0.ugnnf20.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "AQGi8fAAjldmHnMNoxYD6oEijUN38EKtgjP9ISs7tnqb0xreMSBYP2kOPBpl_SIUtWGBoDkLPfp51mGRc20yHLyORYCDuxBg3i9Mvs76kUjWTjHBB9icRuZ2QSfhPAqnSLb472TU6Owz1CTWx6hJqMEt4iGov4FgzH37IGsJ5OKCVnV8AMfBfdjNZExHUg2RenClC1EXpCiGWY9i4Luu8ykljMil33UKfl8DphqcFqeBGTJH06_mDh0upvtxxCl4LBh6aJxKFL5MvLB_nBmmLbPSSUuKqPs4O8ofL2LfVd_PwlQq7dIHMLR0lI25emV4yIh-94FUqNkUdw6HUJ9oCq5qXAUZpAAAAAByirZPAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002156297566"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
