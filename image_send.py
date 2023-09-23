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
      nftSaleTransactions {
        nfts {
          tokenAmount
        }
      }
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
    for search_result_index in range(0,len(query_response.data['TokenNfts']['TokenNft'])):
        current_token_address.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['address'])
        tokenId.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['tokenId'])
        image.append(query_response.data['TokenNfts']['TokenNft'][search_result_index]['contentValue']['image']['large'])
    print(current_token_address)
    print(tokenId)
    print(image)
    print("\n\n\n")
    print(query_response.data)
    return image[0]

asyncio.run(name_send("0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"))

