from airstack.execute_query import AirstackClient
import asyncio

async def name_send():
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
}            
"""
    variables =  {
       "address":"0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
}
    
    execute_query_client  = api_client.create_execute_query_object(query = query, variables = variables)
    query_response = await execute_query_client.execute_query()
    current_token_address = query_response.data['TokenNfts']['TokenNft'][0]['address']
    tokenId = query_response.data['TokenNfts']['TokenNft'][0]['tokenId']
    image = query_response.data['TokenNfts']['TokenNft'][0]['contentValue']['image']['large']
    print(current_token_address)
    print(tokenId)
    print(image)

asyncio.run(name_send())