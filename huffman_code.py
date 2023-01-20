"""
Name: Aiden Teal
SID: 1724406
CCID: ateal
AnonID: 1000332190
CMPUT 274, Fall 2022

Assessment: Assignment #2: Huffman Coding """

""" 
import bitio
import huffman """
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''

    tree = pickle.load(tree_stream)

    return tree

    pass


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """

    # Traverses the tree while reading bits until it hits a Leaf Node
    while type(tree) == (huffman.TreeBranch or huffman.TreeLeaf):
        bits_read = bitreader.readbit()
        # if the bit is 0, this stands for False or traverse left
        if bits_read == 0:
            tree = tree.getLeft()
        # if the bit is 1, this stands for True or traverse Right
        elif bits_read == 1:
            tree = tree.getRight()
        # if a leaf is found, it will return the value of the leaf
        if type(tree) == huffman.TreeLeaf:
            return tree.getValue()
    pass


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''

    # Defines the bito.BitReader instance using the compressed stream
    Bit_Reader = bitio.BitReader(compressed)
    # Defines the bitio.BitWriter instance using the uncompressed stream
    Bit_Writer = bitio.BitWriter(uncompressed)

    huff_tree = read_tree(compressed)
    decoding = decode_byte(huff_tree, Bit_Reader)

    # Decodes the stream, using the huffman tree and writes the symbols
    # to the uncompressed stream. Stops at EOF/None value
    while decoding is not None:
        Bit_Writer.writebits(decoding, 8)
        decoding = decode_byte(huff_tree, Bit_Reader)

    pass


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''

    pickle.dump(tree, tree_stream)

    pass


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''

    write_tree(tree, compressed)

    Bit_Reader = bitio.BitReader(uncompressed)
    Bit_Writer = bitio.BitWriter(compressed)

    table = huffman.make_encoding_table(tree)

    writing = True
    while writing:
        try:
            # Writes the bits from uncompressed stream into the
            # compressed stream
            for one_bit in table[Bit_Reader.readbits(8)]:
                if one_bit is False:
                    Bit_Writer.writebit(False)
                else:
                    Bit_Writer.writebit(True)
            # if EOFError is raised, it will write the None bit for the EOF
            # and then quit writing
        except EOFError:
            for EOFbit in table[None]:
                if EOFbit is False:
                    Bit_Writer.writebit(False)
                else:
                    Bit_Writer.writebit(True)
            writing = False

    # flushes the bitwriter to remove any partially-written bits
    Bit_Writer.flush()
    pass
