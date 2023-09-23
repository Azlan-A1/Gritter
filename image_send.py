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
        current_token_address.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['address'])
        tokenId.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['tokenId'])
        image.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['contentValue']['image']['large'])
    for search_result_index in range(0, len(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"])):
        transactionhash.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["transactionHash"])
        blocktimestamp.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["blockTimestamp"])
        payment_eth.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInNativeToken"])
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

asyncio.run(name_send("0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"))

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