from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1268fill---your----data"
	APP_ID = 1373938
	API_HASH = "fill--your--data"
	OWNER_ID = "" #ID of bot owner
	AUTH_CHANNEL = [-10082786282972]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAXMBZvEyehWLtikrbpVlCaAuH6_LepyL9xOJpxYwsPpHrVqeOAK8f1Fkd3o4eOntS8ae6moAL5JLNIqlSo9ZpQO7cOCXxxRfFSfG3DqD1KMzicUeBSf7JzUfiLYEnOMly8O27oyRT_mbhup4FYAoC5-HegaFA:"Bearer","refresh_token":"1//0ds6warEInR1LCgYIARAAGA0SNwF-L9IrgkM5-Q-N2IMWX_4EFrHEgwTgfkJ0LCBgB9jzb2YEg78A6fPXhP9IzOG91Z18SdrzAmU","expiry":"1597147591898"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
