import tensorflow as tf
a = 1
b = [1,2,3]
c=[[1,2],[1,2]]
print(tf.shape(a))
print(tf.shape(b))
print(tf.shape(c))



# tensor = decode_png("C:\\Users\\FIRAT\\Desktop\\1.png");
#bu resim okuyor...
image = tf.image.decode_png(tf.read_file('C:\\Users\\FIRAT\\Desktop\\1.png'),1)
sess = tf.Session()
print(sess.run(image))
