#First_File_Sync_script

import os
import shutil
import filecmp
import argparse
import logging

def setup_logging(log_file_path):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )

def log_action(message):
    logging.info(message)


#I am now going to use this check_directories() function to check if the source and replica directories exist

def check_directories(source_dir, replica_dir):
    if not os.path.exists(source_dir):
        log_action(f"Source directory '{source_dir}' does not exist.")
        return False
    #then I will create the replica if it does not exist
    if not os.path.exists(replica_dir):
        os.makedirs(replica_dir)
        log_action(f"Destination directory '{replica_dir}' created.")
    return True

# this function will Synchronize Files Between Directories , its called the Sync_directories function
# handles this task by first going through the source directory to gather a list of all files and subdirectories. handles this task by first going through the source directory to gather a list of all files and subdirectories.

def sync_directories(source_dir, replica_dir, delete =False):
    # get a list of all files and directories in the source directory

    files_to_sync=[]
    for root, dirs ,files in os.walk(source_dir):
        for directory in dirs:
            files_to_sync.append(os.path.join(root, directory))
        for file in files:
            files_to_sync.append(os.path.join(root, file))

        #Iterate over each file in the source directory 
        # i will now iterate over each file in the source directory

        for source_path in files_to_sync: # I will now fetch the corresponding path in the replica directory
          replica_path = os.path.join(replica_dir , os.path.relpath(source_path, source_dir)) 

          #os.path.relpath ,meaning relative path returns a relative 
          #filepath to the given path either from the current working directory or from the given directory

          # I will now check if the path is a directory and if not create it in the replica directory 
          if os.path.isdir(source_path):
              if not os.path.exists(replica_path):
                  os.makedirs(replica_path)

          # Copy all the source directory to the replica  directory
          else:
              #check if the file exists in the replica directory and if it is different from the source file
              if not os.path.exists(replica_path) or not filecmp.cmp(source_path, replica_path, shallow=False):
                  
                  log_action(f"Copying '{source_path}' to '{replica_path}'")

                  # I will now copy file from the source directory to the replica directory
                  shutil.copy2(source_path, replica_path)


# Now I shall clean up extra files in the replica directory if they are not in the source directory , using a delete flag

    if delete:
      # Getting a list of all files in the destination directory
      files_to_delete =[]
      for root,dirs,files in os.walk(replica_dir):
          for directory in dirs:
              files_to_delete.append(os.path.join(root, directory))
          for file in files:
              files_to_delete.append(os.path.join(root, file))

      #I will now iterate over each file in the destination directory
 
      # Now I show iterate over each file in the destination directory
      for replica_path in files_to_delete:
           # now I will check if the files in the source directory
           source_path = os.path.join(source_dir, os.path.relpath(replica_path, replica_dir))
           if not os.path.exists(source_path):
               log_action(f"Deleting '{replica_path}'")

               #checking if the path is a directory and remove it
               if os.path.isdir(replica_path):
                   shutil.rmtree(replica_path) #shutil.rmtree is used to remove entire tree
                
               else:
                   # removing the file from the destination directory
                   os.remove(replica_path)

# The script is designed to be run from the command line, with arguments specifying the source and destination directories.

# The argparse module makes it easy to handle these arguments, allowing users to simply provide the necessary paths and options when running the script.
          

if __name__ == "__main__":
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description="Synchronize files between two directories.")
    parser.add_argument("source_directory", help="The source directory to synchronize from.")
    parser.add_argument("destination_directory", help="The destination directory to synchronize to.")
    parser.add_argument("-d", "--delete", action="store_true",help="Delete files in destination that are not in source.")
    parser.add_argument("-l", "--log", required=True,help="Path to the log file.")
    
    args = parser.parse_args()
    log_file_path = args.log
    setup_logging(log_file_path)

    # If the delete flag is set, logging a warning message
    if args.delete:
        log_action("Extraneous files in the destination will be deleted.")

    # Check the source and destination directories
    if not check_directories(args.source_directory, args.destination_directory):
        exit(1)

    # Synchronize the directories
    sync_directories(args.source_directory, args.destination_directory, args.delete)
    log_action("Synchronization complete.")
