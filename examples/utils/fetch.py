import tensorflow as tf

def read():
    filename_queue = tf.train.string_input_producer([r"C:\Users\FIRAT\Desktop\Transport_Mode_Detection\csv\deneme.csv"])

    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)

    # Default values, in case of empty columns. Also specifies the type of the
    # decoded result.
    record_defaults = [tf.constant([]),
                       tf.constant([]),
                       tf.constant([]),
                       tf.constant([]),
                       tf.constant([]),
                       tf.constant([])]

    ACC_MINRED, ACC_MAXRED, ACC_MININC, ACC_MAXINC, ACC_MINVAL, ACC_MAXVAL = tf.decode_csv(value,
                                                                                           record_defaults=record_defaults)
    features = tf.stack([ACC_MINRED, ACC_MAXRED, ACC_MININC, ACC_MAXINC, ACC_MINVAL, ACC_MAXVAL])

    with tf.Session() as sess:
        # Start populating the filename queue.
        tf.initialize_all_variables().run()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        row = sess.run([features])
        # print(row[0])
        # for i in range(1,10):
        #   # Retrieve a single instance:
        #   row = sess.run([features])
        #   print(row)
        #   # example, label1 = sess.run([features, ACC_MAXRED])
        #   # print(label);
        coord.request_stop()
        coord.join(threads)
        print(row[0])
        return row[0]
