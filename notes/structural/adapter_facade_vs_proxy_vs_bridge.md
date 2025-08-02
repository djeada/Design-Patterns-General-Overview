 # Adapter vs facade vs proxy vs bridge

- FACADE is just an interface, it's not even a pettern, more like a good approach (AN HTTP API abstracts away the network details, data structures are facade)

Design to interfaces
– Façade – a new interface for a library
– Adapter – design application to a common interface, adapt other
libraries to that
• Favor composition over inheritance• Favor composition over inheritance
– Façade – library is composed within Façade
– Adapter – adapter object interposed between client and
implementation
• Find what varies and encapsulate it
– Both Façade and Adapter – shields variations in the implementation
from the client

Motivation
– Façade: simplify the interface
– Adapter: match an existing interface
• Adapter: interface is given• Adapter: interface is given
– Not typically true in Façade
• Adapter: polymorphic
– Dispatch dynamically to multiple implementations
– Façade: typically choose the implementation statically
