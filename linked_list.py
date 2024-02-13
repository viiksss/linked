class LinkedList: 
 
    class Item: 
        value = None 
        next = None 
 
        def __init__(self, value): 
            self.value = value 
 
    head:Item = None 
     
    def append_begin(self, value): 
        item = LinkedList.Item(value) 
        item.next = self.head 
        self.head = item 
 
    def append_end(self, value): 
        current = self.head 
        if current is None: 
            self.head = LinkedList.Item(value) 
            self.head.value = value 
            return 
         
        while current.next: 
            current = current.next 
         
        item = LinkedList.Item(value) 
        current.next = item 

    def append_by_index(self,value,index):
        if index<0:
            raise ValueError("Индекс не может быть отрицательным")
        if index == 0:
            self.append_begin(value)
            return
        current = self.head
        dd = None
        count = 0
        while current and count < index:
            dd = current
            current = current.next
            count+=1
            if count < index:
                raise IndexError("Индекс вне диапазона")
            item = LinkedList.Item(value)
            dd.next = item
            item.next = current

     
    def __len__(self): 
        count = 0 
        current=self.head 
        while current: 
            count+=1 
            current=current.next 
        return count 
         
    def remove_first(self): 
        if self.head == None: 
            raise ValueError("Список пуст") 
        self.head=self.head.next 
 
    def remove_last(self): 
        if self.head == None: 
            raise ValueError("Список пуст") 
        if self.head.next is None: 
            self.head = None 
            return 
        current = self.head 
        while current.next: 
            current = current.next 
            current.next = None 
    
    def remove_at(self,index):
        if self.head == None:
            raise ValueError("Список пуст")
        if index == 0:
            self.head == self.head.next
            return
        current = self.head
        dd = None
        count = 0
        while current and count<index:
            dd= current
            current = current.next
            count+=1
        if current is None:
            raise ValueError("Индекс вне диапазона")
        dd.next=current.next
        
    def remove_first_value(self,value):
        if self.head.value == value:
            raise ValueError("Список пуст")
        if self.head.value == value:
            self.head == self.head.next
            return
        current = self.head
        dd = None
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                dd = current
                current = current.next
        if not found:
            raise ValueError("Этого значения нет в списке")
        dd.next == current.next
    
    def remove_last_value(self,value):
        if self.head == None:
            raise ValueError("Список пуст")
        if self.head.value == value and self.head.next is None:
            self.head = None
            return
        current = self.head
        dd = None
        last = None
        found = False
        while current:
            if current.value == value:
                dd = last
                found = True
                last = current
                current = current.next
        if not found:
            raise ValueError("Этого значения нет в списке")
        if dd is None:
            self.head = last.next
        else:
            dd.next = last.next

    def get_count(self):
        count=0
        current = self.head
        while current:
            count+=1
            current = current.next
            return count
        

 
 
 
 
        
my_list=LinkedList() 
my_list.append_begin(1) 
my_list.append_begin(4) 
my_list.append_begin(5)
my_list.append_begin(5)
my_list.append_by_index(10,1)
my_list.remove_last() 
my_list.remove_first() 
my_list.remove_at(0)
my_list.remove_last_value(5)
my_list.remove_first_value(1)
my_list.get_count()
print(len(my_list))
print("Конечный результат:", my_list)