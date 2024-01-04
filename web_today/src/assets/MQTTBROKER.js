var mosca = require('mosca');
var auth = new mosca.Authorizer();
var settings = {
port: 3003,

};

var server = new mosca.Server(settings);
server.on('clientConnected', function(client) {
   console.log('client connected', client.id);
});
server.on('ready', function(){
	
	
console.log("ready");
server.authenticate = auth.authenticate; //
    //server.authorizePublish = auth.authorizePublish;//
    //server.authorizeSubscribe = auth.authorizeSubscribe;//
//adduser 
auth.addUser('PLCS71500','12345','presence', 'presence',function(error){
        if(error){
            console.log('auth add user error:' + error);
        }else{
            console.log("auth add user tronghd1 success");
        }
		 })
});

//find when a message is received
server.on('published',function getdata(packet,client) {
  
  //var data = packet.payload.toString();
	//var jsondata = JSON.parse(data);
	//console.log('simulate_var2',jsondata);
	//console.clear();
if(packet.topic =='ATW1') 
{
	//console.log('MobusRTU/Slave1: ', packet.payload);
	//var data = packet.payload.toString();
	//var jsondata = JSON.parse(data);
	//console.log('data PLC: ',jsondata);
	//console.log('data PLC: ',jsondata.name );
}
/*if(packet.topic =='topic1' ) 
{
	var data = packet.payload.toString();
	//var jsondata = JSON.parse(data);
	console.log('data nhan: ',data  );
	
	//var jsondata = JSON.parse(data);
	//console.log('simulate_var2',jsondata);
}
if(packet.topic =='topic2' ) 
{
	var data = packet.payload.toString();
	//var jsondata = JSON.parse(data);
	console.log('data nhan2: ',data  );
	
	//var jsondata = JSON.parse(data);
	//console.log('simulate_var2',jsondata);
}*/
/* if(packet.topic =='Data/MSB_02') 
{
	console.log('topic 2: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/SB_B2') 
{
	console.log('topic 3: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/SB_B3') 
{
	console.log('topic 4: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/SB_B5') 
{
	console.log('topic 5: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/Stenter_01') 
{
	console.log('topic 6: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/Stenter_02') 
{
	console.log('topic 7: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/SBB_01') 
{
	console.log('topic 8: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
}
if(packet.topic =='Data/Tranfor') 
{
	console.log('topic 9: ', packet.topic);
	var data = packet.payload.toString();
	var jsondata = JSON.parse(data);
	console.log('simulate_var2',jsondata);
} */

   
});

