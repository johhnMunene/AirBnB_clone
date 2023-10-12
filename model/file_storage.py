import json
from model.base_model import BaseModel






class FileStorage:
      __file_path = "file.json"
      __objects = {}
      
      def all(self,line):
         return 