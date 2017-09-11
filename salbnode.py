class SALBnode:
    """Node for linked list representation of snakes and ladders board."""
    def __init__(self: 'SALBnode', next: 'SALBnode' = None,
                 snadder: 'SALBnode' = None) -> None:
        # Representation invariant:
        #  self.next points to the next SALBnode.
        #  If self.snadder!=None, then self is the source of a snadder
        #   whose desination is self.snadder.
        #  If self.snadder==None, then self is not the source of a snadder.
        self.next = next
        self.snadder = snadder

       
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
