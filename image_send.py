from airstack.execute_query import AirstackClient
import asyncio

from flask import Flask, request, render_template



#address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

async def name_send(address):
    
    api_client = AirstackClient(api_key = "ef3d1cdeafb642d3a8d6a44664ce566c")
    query="""
query MyQuery( $address: Address) {
  TokenNfts(input: {blockchain: ethereum, filter: {address: {_eq: $address}}}) {
    TokenNft {
      tokenId
      metaData {
        name
      }
      blockchain
      address
      contentValue {
        image {
          large
        }
      }
      
    }
  }
  NFTSaleTransactions(
    input: {filter: {nfts: {tokenAddress: {_eq: $address}}}, blockchain: ethereum, limit: 20, order: {blockTimestamp: DESC}}
  ) {
    NFTSaleTransaction {
      formattedPaymentAmountInNativeToken
      formattedPaymentAmountInUSDC
      transactionHash
      blockTimestamp
    }
  }
}            
"""
    variables =  {
       "address":address
}
    
    execute_query_client  = api_client.create_execute_query_object(query = query, variables = variables) 
    query_response = await execute_query_client.execute_query()
    if query_response is None:
        return "There are no nft's in this address"
    if query_response.data['TokenNfts']['TokenNft'] is None:
        return "Again there are no nft's in this address"
    
    current_token_address = []
    tokenId = []
    image = []
    transactionhash = []
    blocktimestamp = []
    payment_eth = []
    payment_usdc = []
    average_eth = 0
    average_usdc = 0
    for search_result_index in range(0,len(query_response.data['TokenNfts']['TokenNft'])):
        try:
            current_token_address.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['address'])
        except:
            current_token_address[search_result_index]= "No address found"
        else:
            current_token_address.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['address'])
        try:
            tokenId.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['tokenId'])
        except:
            tokenId[search_result_index] = "No Id found"
        else:
            tokenId.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['tokenId'])
        try:
            image.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['contentValue']['image']['large'])
        except:
            image.append("http://www.clker.com/cliparts/n/T/5/z/f/Y/image-missing-md.png")
        else:
            image.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['contentValue']['image']['large'])
    if query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"] is not None:
        for search_result_index in range(0, len(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"])):
            try:
                transactionhash.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["transactionHash"])
            except:
                transactionhash[search_result_index] = "No transaction hash found"
            else:
                transactionhash.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["transactionHash"])
            try:
                blocktimestamp.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["blockTimestamp"])
            except:
                blocktimestamp[search_result_index] = "No time stamp found"
            else:
                blocktimestamp.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["blockTimestamp"])
            try:
                payment_eth.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInNativeToken"])
            except:
                payment_eth[search_result_index] = "No eth payment found"
            else:
                payment_eth.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInNativeToken"])
            try:
                payment_usdc.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInUSDC"])
            except:
                payment_usdc[search_result_index] = "No usdc payment values found"
            else:
                payment_usdc.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInUSDC"])
             
           
           
            average_eth+=payment_eth[search_result_index]
            average_usdc+=payment_usdc[search_result_index]
        average_eth = average_eth/len(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"])
        average_usdc = average_usdc/len(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"])
    
    print(current_token_address)
    print(tokenId)
    print(image)
    print("\n\n\n")
    print(payment_usdc)
    print("\n\n\n")
    print(average_eth)
    print(average_usdc)
    print("\n\n\n")
    print(query_response.data)
    return image[0]

asyncio.run(name_send("0x343f999eAACdFa1f201fb8e43ebb35c99D9aE0c1"))

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/search', methods=['POST'])
# def search():
    
#     search_term = request.form.get('search_term')
#     print("Search term entered:", search_term)
#     image_url = asyncio.run(name_send(search_term))

#     return "search term received: "+search_term+ " image url is: " + image_url + render_template('search_results.html', search_term=search_term, image_url=image_url)

# if __name__ == '__main__':
#     app.run(debug=True)