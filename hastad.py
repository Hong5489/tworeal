#!/usr/bin/env python2.7
from Crypto.Util.number import GCD, bytes_to_long, long_to_bytes, inverse
import gmpy2

def crt(list_a, list_m):
    """
    Reference: https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    Returns the output after computing Chinese Remainder Theorem on
    x = a_1 mod m_1
    x = a_2 mod m_2
    ...
    x = a_n mod m_n
    input parameter list_a = [a_1, a_2, ..., a_n]
    input parameter list_m = [m_1, m_2, ..., m_n]
    Returns -1 if the operation is unsuccessful due to some exceptions
    """
    for i in range(len(list_m)):
        for j in range(len(list_m)):
            if GCD(list_m[i], list_m[j])!= 1 and i!=j:
                raise Exception("Moduli should be pairwise co-prime")
                
    M = 1
    for i in list_m:
        M *= i
    list_b = [M//i for i in list_m]
    assert len(list_b) == len(list_m)
    try:
        list_b_inv = [inverse(list_b[i], list_m[i]) for i in range(len(list_m))]
    except:
        raise Exception("Encountered an unusual error while calculating inverse")
        
    x = 0
    for i in range(len(list_m)):
        x += list_a[i]*list_b[i]*list_b_inv[i]
    return x % M


def test_crt():
    """
    Checking the validity and consistency of CRT function
    """
    list_a = [[2, 3], [1, 2, 3, 4], [6, 4]]
    list_m = [[5, 7], [5, 7, 9, 11], [7, 8]]
    soln_list = [17, 1731, 20]
    try:
        for i in range(len(list_a)):
            assert crt(list_a[i], list_m[i]) == soln_list[i]
    except:
        print("[+] CRT function broken. Check the function again!")


def hastad_unpadded(ct_list, mod_list, e):
    """
    Implementing Hastad's Broadcast Attack
    """
    m_expo = crt(ct_list, mod_list)
    if m_expo != -1:
        eth_root = gmpy2.iroot(m_expo, e)
        if eth_root[1] == False:
            raise Exception("Cannot calculate e'th root!")
        elif eth_root[1] == True:
            return str(long_to_bytes(eth_root[0]))[2:-1]
    else:
        raise Exception("Cannot calculate CRT")
# n1 = 7156756869076785933541721538001332468058823716463367176522928415602207483494410804148006276542112924303341451770810669016327730854877940615498537882480613
# n2 = 11836621785229749981615163446485056779734671669107550651518896061047640407932488359788368655821120768954153926193557467079978964149306743349885823110789383
# n3 = 7860042756393802290666610238184735974292004010562137537294207072770895340863879606654646472733984175066809691749398560891393841950513254137326295011918329
# c1 = 816151508695124692025633485671582530587173533405103918082547285368266333808269829205740958345854863854731967136976590635352281190694769505260562565301138
# c2 = 8998140232866629819387815907247927277743959734393727442896220493056828525538465067439667506161727590154084150282859497318610746474659806170461730118307571
# c3 = 3488305941609131204120284497226034329328885177230154449259214328225710811259179072441462596230940261693534332200171468394304414412261146069175272094960414
# print(hastad_unpadded([c1,c2,c3],[n1,n2,n3],3))