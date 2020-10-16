import React from 'react'
import  { MongoClient } from "mongodb";
const clientPEMFile = null
const monGOD_options = {
	protocol: "mongodb+srv",
	credentials: '',
	hostname:'',
	port:'',
	additional_options: {
		authMechanism :"MONGODB-X509",
		tls:true,
		tlsCertificateKeyFile:clientPEMFile,
		validateOptions:20,
		w:"majority",
		validateOptions:null,
		family:null,
		noDelay:null,
		clientPEMFile:null,
		keepAlive:null,
		keepAliveInitialDelay:null,
		connectTimeoutMS:null,
		socketTimeoutMS:null,
		forceServerObjectId:null,
		serializeFunctions:null,
		ignoreUndefined:null,
		raw	:null,
		promoteLongs:null,
		promoteBuffers:null,
		promoteValues:null,
		pkFactory:null,
		promiseLibrary:null,
		loggerLevel:null,
		logger:null,
		}
	}
const _protocol =  _version = 4.2? ssl:tls
const _macOS = "macOS, you cannot disable TLS1_1 and leave both TLS1_0 and TLS1_2 enabled. You must disable at least one of the other two, for example, TLS1_0,TLS1_1."
const net = {
	ssl:{
		disabledProtocols= ['TLS1_3','TLS1_2','TLS1_1','TLS1_0'],
		},
	tls: {
		FIPSMode ,
		disabledProtocols=['TLS1_3','TLS1_2','TLS1_1','TLS1_0'],
		}
	}	
net.ssl.disabledProtocols= ['TLS1_3','TLS1_2','TLS1_1','TLS1_0']
const {protocol, credentials, hostname, port, additional_options} = monGOD_options
const uri = `${protocol}://${credentials}@${hostname:port}/?${/** Create a loop for non null values*/}`
const client = new MongoClient(uri);
export  async function run() {
  try {
    // Connect the client to the server
    await client.connect();

    // Establish and verify connection
    await client.db("admin").command({ ping: 1 });
    console.log("Connected successfully to server");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);

const MongoDBClientSide = props => {
	return <h1>"MongoDB Client Side"</h1>
	
	}
export default MongoDBClientSide
