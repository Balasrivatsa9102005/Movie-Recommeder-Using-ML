import pickle
import os

# Function to split pickle file into chunks
def split_pickle(file_path, chunk_size=500):
    with open(file_path, 'rb') as file:
        # Load the pickle data
        similarity_data = pickle.load(file)
        
    # Get the total number of items in the data
    total_items = len(similarity_data)
    
    # Create a folder for the chunks
    folder_name = file_path.split('.')[0]  # Folder name same as file base name
    os.makedirs(folder_name, exist_ok=True)
    
    print(f"Chunks will be saved in: {folder_name}")  # Added print to confirm the folder
    
    # Split the data into chunks and save
    chunk_count = 0
    for i in range(0, total_items, chunk_size):
        chunk_count += 1
        chunk_data = similarity_data[i:i + chunk_size]
        chunk_file_name = f'{folder_name}/similarity_chunk_{chunk_count}.pkl'
        
        with open(chunk_file_name, 'wb') as chunk_file:
            pickle.dump(chunk_data, chunk_file)
    
    print(f"Pickle file split into {chunk_count} chunks in the folder: {folder_name}.")

# Split the similarity.pkl file
split_pickle('C:/Users/balas/OneDrive/Desktop/Balu/Myprojects/vs/MovieRecommendation/similarity.pkl')
