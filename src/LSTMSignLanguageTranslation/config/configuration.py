from LSTMSignLanguageTranslation.constants import *
from LSTMSignLanguageTranslation.utils.common import read_yaml, create_directories
from LSTMSignLanguageTranslation.entity.config_entity import (DataIngestionConfig, 
                                                         LandmarksExtractionConfig, 
                                                         PreprocessingConfig, 
                                                         PrepareBaseModelConfig,
                                                         ModelTrainerConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
        
        )

        return data_ingestion_config