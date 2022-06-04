# Author: Remington Brandenburger
# Date: April 2022
# Description: main.py manages the function calling for the collection, processing, and uploading of data.


import raw_broadcast_loader as rawBroadcastLoader
from broadcast_data_utilites import broadcast_object_generator
import os

if __name__ == '__main__':
  print('Running App...')

  #TODO: Tell radio to listen for airplanes ( 5 min duration )

  #SDR outputs broadcast data in CSV files
  currentPath = os.path.dirname(__file__)
  dataFilePath = os.path.join(currentPath, ".\\sample_data\\sample_data.csv")
  rawBroadcasts = rawBroadcastLoader.read_data_from_file(dataFilePath)

  #Generate broadcast objects from raw hex data
  broadcasts = []
  for x in rawBroadcasts:
    broadcasts.append(broadcast_object_generator.generate_broadcast(x))

  #TODO: Delete me
  for x in broadcasts:
    print(x)

  #TODO: process list of broadcast objects, and update DB
  print('App processess completed')