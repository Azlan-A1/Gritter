from airstack.execute_query import AirstackClient
import asyncio

#from flask import Flask, request, render_template



address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

async def name_send(address):
    
    api_client = AirstackClient(api_key = "ef3d1cdeafb642d3a8d6a44664ce566c")
    #Uses demo key from python SDK files
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
#Query uses the AI integration on the airstack search model to collect information on the nft's image, token id, token address, blockchain status, how much was paid during transactions of the nfts including the block time stamp and transaction hash.
    variables =  {
       "address":address
}
    
    execute_query_client  = api_client.create_execute_query_object(query = query, variables = variables) 
    
    query_response = await execute_query_client.execute_query()
    #execute_query turns the object into readable data
    if query_response is None:
        return "There are no nft's in this address"
    if query_response.data['TokenNfts']['TokenNft'] is None:
        return "Again there are no nft's in this address"
    #Checks if the address did not return any data through the search engine
    current_token_address = []
    tokenId = []
    image = []
    transactionhash = []
    blocktimestamp = []
    payment_eth = []
    payment_usdc = []
    average_eth = 0
    average_usdc = 0
    #Iterates through the nft collection and puts every result in a list.
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
                payment_eth[search_result_index] = 0
            else:
                payment_eth.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInNativeToken"])
            try:
                payment_usdc.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInUSDC"])
            except:
                payment_usdc[search_result_index] = 0
            else:
                payment_usdc.append(query_response.data["NFTSaleTransactions"]["NFTSaleTransaction"][search_result_index]["formattedPaymentAmountInUSDC"])
            #try and excepts in case only one nft did not return any data or values.
           
           
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
    print(transactionhash)
    print("\n\n\n")
    print(query_response.data)
    return image[0]

asyncio.run(name_send(address))