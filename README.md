# Google Search API using Colab as a Proxy Server

This repository provides a solution to bypass Google rate limits using Google Search API in conjunction with Colab and ngrok as a proxy server.

## Prerequisites

### Step 1: Create an ngrok Account
1. **Sign Up or Log In**  
   - Create an account [here](https://dashboard.ngrok.com/signup) or log in [here](https://dashboard.ngrok.com/login).
2. **Select Python**  
   - On the homepage, select Python.  
   ![Select Python](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/select_python%20(1).png)
3. **Copy Auth Token**  
   - Scroll down and copy the auth token.  
   ![Copy Auth Token](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/copy_auth_token.jpeg)

### Step 2: Set Up Domain and Edge
1. **Select Domain**  
   - In the left sidebar, select Domain.  
   ![Select Domain](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/select_domains.jpeg)
2. **Create a New Domain**  
   - Create a new domain.  
   ![Create Domain](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/select_python%20(2).png)
3. **Copy Domain Name**  
   - Once completed, copy the domain name.  
   ![Copy Domain Name](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/copy_doman_name.jpeg)
4. **Select Edges**  
   - In the left sidebar, select Edges.  
   ![Select Edges](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/select_edges.jpeg)
5. **Delete Existing Edges**  
   - Ensure there are no edges. If there are, delete them.  
   ![Delete Edges](https://github.com/avijitbhuin21/Google_Search_api/blob/main/readme_photos/delete_edges.jpeg)

### Step 3: Set Up Colab
1. **Open Colab**  
   - Open this [Colab notebook](https://colab.research.google.com/drive/1mQMDGWL1J-gIsjdDcgg6P_HxfKTX463m?usp=sharing) or create a new Colab and copy the code from the `server.py` file in this [GitHub repository](https://github.com/avijitbhuin21/Google_Search_api/blob/main/server.py).
2. **Keep Colab Alive**  
   - Click on inspect on the Colab, open the console, and paste the following JS code: [keep_alive.js](https://github.com/avijitbhuin21/Google_Search_api/blob/main/keep_alive.js).
3. **Replace Auth Token and Domain**  
   - Replace the ngrok auth token and ngrok domain name in the code.
4. **Run Colab**  
   - If everything is done correctly, there should be no errors when running the Colab notebook.

### Step 4: Set Up Client
1. **Copy Client Code**  
   - Copy the `client.py` from this [GitHub repository](https://github.com/avijitbhuin21/Google_Search_api/blob/main/client.py) to your local machine or a different Colab.

## Usage

```python
from client import Bulk_Scrapper

# Replace 'Your Ngrok Domain Here' with your actual ngrok domain
Scraper = Bulk_Scrapper('Your Ngrok Domain Here')

# Example usage
urls = Scraper.Scrape(['words', 'hii'])
for i in urls:
    print(i, urls[i])
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

---

If you have any questions or need further assistance, please feel free to open an issue on the GitHub repository.

Happy Scraping!


