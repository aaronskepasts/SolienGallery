// import * as web3 from '@solana/web3.js';
// const readline = require('readline-sync');


const web3 = require('@solana/web3.js');
const base58 = require('bs58');


// const PubKeysInternedMap = new Map<string, PublicKey>();

// const toPublicKey = (string) => {
//   if (typeof key !== "string") {
//     return key;
//   }
//   var PubKeysInternedMap = new Map<string, web3.PublicKey>();
//   let result = PubKeysInternedMap.get(key);
//   if (!result) {
//     PubKeysInternedMap.set(key, result);
//   }
//
//   return result;
// };
//
// async function getMetadataKey(
//   tokenMint: StringPublicKey
// ): Promise<StringPublicKey> {
//   const PROGRAM_IDS = programIds();
//
//   return (
//     await findProgramAddress(
//       [
//         Buffer.from(METADATA_PREFIX),
//         toPublicKey(PROGRAM_IDS.metadata).toBuffer(),
//         toPublicKey(tokenMint).toBuffer(),
//       ],
//       toPublicKey(PROGRAM_IDS.metadata)
//     )
//   )[0];
// }

// const METADATA_SCHEMA = new Map<any, any>([
//   [
//     Data,
//     {
//       kind: "struct",
//       fields: [
//         ["name", "string"],
//         ["symbol", "string"],
//         ["uri", "string"],
//         ["sellerFeeBasisPoints", "u16"],
//         ["creators", { kind: "option", type: [Creator] }],
//       ],
//     },
//   ],
//   [
//     Creator,
//     {
//       kind: "struct",
//       fields: [
//         ["address", [32]],
//         ["verified", "u8"],
//         ["share", "u8"],
//       ],
//     },
//   ],
//   [
//     Metadata,
//     {
//       kind: "struct",
//       fields: [
//         ["key", "u8"],
//         ["updateAuthority", [32]],
//         ["mint", [32]],
//         ["data", Data],
//         ["primarySaleHappened", "u8"],
//         ["isMutable", "u8"],
//       ],
//     },
//   ],
// ]);

// class Metadata {
//   key: MetadataKey;
//   updateAuthority: PublicKey;
//   mint: PublicKey;
//   data: Data;
//   primarySaleHappened: boolean;
//   isMutable: boolean;
//   masterEdition?: PublicKey;
//   edition?: PublicKey;
//   constructor(args: {
//     updateAuthority: PublicKey;
//     mint: PublicKey;
//     data: Data;
//     primarySaleHappened: boolean;
//     isMutable: boolean;
//     masterEdition?: PublicKey;
//   }) {
//     this.key = MetadataKey.MetadataV1;
//     this.updateAuthority = args.updateAuthority;
//     this.mint = args.mint;
//     this.data = args.data;
//     this.primarySaleHappened = args.primarySaleHappened;
//     this.isMutable = args.isMutable;
//   }
// }

// const decodeMetadata = (buffer: Buffer): Metadata => {
//   const metadata = deserializeUnchecked(
//     METADATA_SCHEMA,
//     Metadata,
//     buffer
//   ) as Metadata;
//
//   metadata.data.name = metadata.data.name.replace(/\0/g, "");
//   metadata.data.symbol = metadata.data.symbol.replace(/\0/g, "");
//   metadata.data.uri = metadata.data.uri.replace(/\0/g, "");
//   metadata.data.name = metadata.data.name.replace(/\0/g, "");
//   return metadata;
// };

function getWallet(){
(async () => {
  // Connect to cluster
  try {
    var connection = new web3.Connection(
      web3.clusterApiUrl('mainnet-beta')


    );

    // // Generate a new wallet keypair and airdrop SOL
    var pubkey = new web3.PublicKey("9YsxYsfZKqTd5upncWtzgaA97qzymPi28aJvwhvq1MDf")
    const metadata = await connection.getAccountInfo(
        pubkey
      );
    // const metadataKey = await getMetadataKey(pubkey.toBase58());
    // const metadataInfo = await connection.getAccountInfo(
    //     toPublicKey(metadataKey)
    // );
    console.log(metadata.data.toString());
    // var airdropSignature = await connection.requestAirdrop(
    //   wallet,
    //   web3.LAMPORTS_PER_SOL,
    // );
    //
    // // //wait for airdrop confirmation
    // await connection.confirmTransaction(airdropSignature);
    //
    // // get account info
    // // account data is bytecode that needs to be deserialized
    // // serialization and deserialization is program specic
    // let account = await connection.getAccountInfo(wallet);
    // console.log(account);
  }
  catch (ex) {
    console.log(ex);
  }

})();
}

function main(){
const args = process.argv.slice(2);
getWallet();

}

if (require.main === module)
   main();