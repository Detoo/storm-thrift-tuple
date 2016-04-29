# Test Storm topology with thrift-defined tuple messages

The tuple values in a [Storm topology](http://storm.apache.org) can be any type as long as they are serializable. 
When passing complex messages between bolts, spouts or even services outside the topology, it is desirable to 
have a strongly typed language-agnostic definition of the message and its services. 
This is where [Apache thrift](http://thrift.apache.org) comes into play.

This project demonstrates the use of thrift-defined messages in a Storm topology. Note as of Storm v2.0.0-snapshot, 
all data exchanged inside a topology is [encoded in JSON](http://storm.apache.org/releases/2.0.0-SNAPSHOT/Multilang-protocol.html), 
which means language-specific object instances cannot be passed directly without implementing some sort of 
string-based serialization. To this end, we use thrift's binary serialization for the message object, then encode it
with base64 to make it ASCII-compatible.


# Usage

```
make compile_thrift
make build_topology
make debug_topology
```
