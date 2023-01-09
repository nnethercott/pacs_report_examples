In this example we show one of the tricky aspects of index set maps - although two vectors may be of the same global size, arithmetic is sometimes undefined.

By design the cpp file is meant to fail at runtime. to resolve the issue present, simply make the index assignment for the index sets the same on each rank! 
