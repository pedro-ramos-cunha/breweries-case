## Import libs ---------------------------------------------------------
import requests as rq
import json
import os

## Setting process configs --------------------------------------------
api_url = "https://api.openbrewerydb.org/v1/breweries"                  # API endpoint URL
headers = {}                                                            # Optional headers (e.g., for authentication)
page = 1                                                                # Page number for pagination (default is 1)
per_page = 200                                                          # Number of items per page (considering API limits)
block_count = 0                                                         # Counter for the number of blocks processed
data_fetched = []                                                       # List to store fetched data
base_dir = os.path.dirname(os.path.abspath(__file__))                   # File Base directory
save_path = os.path.join(base_dir, "..", "data", "breweries_data.json") # Path to save the fetched data (adjust as needed)

# 3. Optional: Ensure the directory exists before saving
os.makedirs(os.path.dirname(save_path), exist_ok=True)
## Function to fetch data from API ----------------------------------
def fetch_data_from_api(url, headers, page, per_page):
    params = {
        'page': page,
        'per_page': per_page
    }
    response = rq.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON data
    else:
        return {"error": {"status_code": response.status_code, "message": response.text,"params": params}}
    
## Main execution-----------------------------------------------------
end_flag = False
while not end_flag:
    data = fetch_data_from_api(api_url, headers, page, per_page)
    
    ##Dumps error data  in case of falure
    if "error" in data:
        error_info = data["error"]
        error_info["block_count"] = block_count
        error_info["headers"] = headers
        print(json.dumps(error_info, indent=4)) 
        break
    
    if not data:  # If no data is returned, we have reached the end
        print("No more data to fetch.")
        end_flag = True
    else:
        data_fetched.extend(data)  # Add fetched data to the list
        if page % 10 == 0:  # Print progress every 10 pages
            block_count += 1
            ## Handling saving json file  according to block count
                ## If is not possible to do it in time, my procedure is to save
                ## blocks of json returned by api in files and labeling acorting 
                ## to block count var. If excution is interrupted, I can restart 
                ## from the last block count and avoid to lose all the data already fetched.

        page += 1  # Move to the next page for the next request


with open(save_path, 'w') as f:
    json.dump(data_fetched, f, indent=4)