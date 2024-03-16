class solution:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class solution:
    def removeElements(self,head:optional[listnode],val:int)->optional[listnode]:
        prev=listnode(0)
        temp=prev
        while head:
            if head.val!=val:
                prev.next=head
                prev=prev.next
           head=head.next
        prev.next=None
        return temp.next