import pandas as pd
from file_operation.file_handler import FileHandler


class PreProcessing:
    def __init__(self, logger_object, table_name):
        self.logger = logger_object
        self.table_name = table_name

    def encode_data(self, data, column):
        """

        :param data:
        :param column:
        :return:
        """

        try:
            self.logger.log(self.table_name, "Starting encoding of data", "Info")
            file_handler = FileHandler(self.table_name, self.logger)
            encoder = file_handler.load_model('OneHotEncoder')
            encoded_data = pd.DataFrame(encoder.transform(data[[column]]))
            data.drop([column], axis=1, inplace=True)
            data = pd.concat([data, encoded_data], axis=1, join='inner')
            self.logger.log(self.table_name, "Encoding complete exiting", "Info")
            return data
        except Exception as e:
            self.logger.log(self.table_name, "An error has ocured while performing encoding. Error: " + str(e), "Error")
            raise e
