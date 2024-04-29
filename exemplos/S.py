class FileManager:
    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def write_file(self, file_name, data):
        with open(file_name, 'w') as file:
            file.write(data)

class DataProcessor:
    def process_data(self, data):
        # Process data here
        return processed_data

    def save_processed_data(self, processed_data):
        file_manager = FileManager()
        file_manager.write_file('processed_data.txt', processed_data)

# Exemplo de uso
data = FileManager().read_file('data.txt')
processed_data = DataProcessor().process_data(data)
DataProcessor().save_processed_data(processed_data)
