# Rolling Reveal for NFTs
## Reveal on mint using a mempool explorer

NFT reveals generally take place after a project has sold out. This tends to be the norm, but what happens when a project doesn't sell out quickly? The team is forced to ramp up marketing efforts, and drive hype for their project. The notion of over-subscribed, massively hyped, NFT projects is not something I am a big fan of. It just feels pump-and-dumpy, and seems to place FOMO before organic community growth.

Now, if a project is using IPFS to store metadata, there is a problem... An early reveal will expose the CID for metadata, allowing clever devs to "explore" the collection, determine which tokenIDs are rare, and snipe those off as more buyers enter the project. This is not entirely fair, and if most buyers knew they had no chance of landing a rare nft, they might think twice about participating. Alternatively, the project could just languish un-revealed. But this is a terrible experience for buyers, who wants to wait months to see their new, spanky, NFT?

Ok. So what is the solution? I propose a rolling reveal. Reveal metadata as tokens are minted. This puts less pressure on immediate sales velocity, allows early minters to see their NFT fter purchase, and avoids unfair shenanigans from clever devs.

In order to accomplish this, we will need to use cloud storage for our metadata and images. Before you go crying about centralized solutions, just hear me out. The initial minting phase would be done on some form of cloud storage(AWS for example), and when the project has sold out, a migration to IPFS would take place. This can come in the form of an announcement, letting your community know that the entire collection is being moved to permanent storage. The token URI is updated in the contract, and no one would know the difference.

Knowing when a token is minted is a little tricky, and there are various ways to accomplish this. For this implementation, I chose to use a mempool explorer, BlockNative. They have a handy tool that allows filtering of function calls from a contract, and firing off a custom webhook when a particular call is identified. We just filter on our NFT contract address, and look for confirmed "mint" receipts. This is cheaper than polling an Infura/Alchemy endpoint endlessly, forever. We point the webhook to our FastAPI app deployed in the cloud, pass in the function call data, and process the reveal.

Making use of web2 infrastructure and tools at this point seems to make sense. We get the best of both worlds by leveraging modern storage products, before transfering over to permanent, decentralized, solutions.

## Tech

- [Amazon S3] - Our pre-sellout storage solution. Use two buckets, one private and one public. On mint, metadata and image are transferred fron private to public
- [BlockNative] - mempool explorer with custom webhooks - blocknative.com
- [FastAPI] - Backend service to perform reveals deployed on AWS
- [Docker] - Package up the app and deploy it where you see fit