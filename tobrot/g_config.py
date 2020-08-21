from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1318996036:AAENTgIUSykg5aZVOG5CFenGWe4F41npWlk"
	APP_ID = 1270718
	API_HASH = "53830b514cb1d0a388c26ea48478d180"
	OWNER_ID = "" #ID of bot owner
	AUTH_CHANNEL = [-1001443143917]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """[Waybetter]
type = drive
scope = drive
token = {"access_token":"ya29.a0AfH6SMAGkw736fFoS7HqGlzawjoOQyPLRVV92CUO8Oox6NDN4F4_NNKZicBPhFc2SNwVxtcA_6pF5o7Oi7YUgB4PogBhju5FlTQbcxUUT88ALqvRSaSDr0i3aRoKUdBBijGLl6KbR5yAKebjQZdcIB6-XiVKDfOnMVU","token_type":"Bearer","refresh_token":"1//0gfzVxdHEtdvACgYIARAAGBASNwF-L9Irjx0eNWpESUtifruY45K27-iIo6std1PBtRA-pSV8VWeQlLjPT5GwxL39a8GzJAKfius","expiry":"2020-08-21T16:20:21.350321011Z"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
