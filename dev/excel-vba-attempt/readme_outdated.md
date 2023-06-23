<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
# Symmetric verus Asymmetric Ciphers  

Auhtor:  Erin James Wills, ejw.data@gmail.com   

![Cryptopgraphy](./images/encryption-python.png)

#### **Purpose**:
Cryptography is a tool used more often than realized.  For example, SSH keys used on a computer are asymmetric ciphers and use algorthims like RSA.  The conceptual process is often described but how the math works for even simple, outdated processes is rarely provided.    This repo explores the mathematical processes involved in a simple Diffie-Hellman Key.

#### **Background**:
Originally, I tried to develop this module to help students of a Data Science Bootcamp understand their public and private SSH keys and how they are used on github/gitlab.  Due to the students experience early in the term is only Excel, I tried to write everything in VBA but quickly realized that the numbers generated through this process become too large for excel and keys could only be slightly larger than single digits before throwing an overflow error.  The script was converted over to Python and it worked much better.

#### **The Math Without One Way Functions**:
This example works with one key issue -- a public key and a partial key must be transferred between the sender and receiver.  The partial key provides the extra information needed to decode the message but anyone could do this by plugging the partial key and public key into the correct equation.  In many cases this is described as asymmetric authentication but it really is not.  I have modified reference [1] to be a bit more believable.  Later, I will show a true asymmetric authication that uses the RSA algorithm.    

$$
\tag{1} Key_{partial,s} = (Key_{+s})^{Key_{*s}} \bmod Key_{+r}
$$

$$
\tag{2} Key_{partial,r} = (Key_{+s})^{Key_{*r}} \bmod Key_{+r}
$$
<br>

$$
\tag{3} Key_{full,s} = (Key_{partial,r})^{Key_{*s}} \bmod Key_{+r}
$$

$$
\tag{4} Key_{full,r} = (Key_{partial,s})^{Key_{*r}} \bmod Key_{+r}
$$
<br>
<br>

The mathematical relationship that makes this work.
$$ 
\tag{4}(g^a \bmod p)^b \bmod \ \ p = (g^b \bmod p)^a \bmod p = g^{ab} \bmod p 
$$

$$
\begin{align*}
where \ \ \ \ a& = b \\
b& = f \\
x& = stuff
\end{align*}
$$


## Authentication Process
1.  Two users must decide that they would like to transfer information but in a secure way.  I will call them the requester and the sender.
    *  In the real world we need to be specific about the roles.  Many times this is overlooked when discussing asymmetric authentication.  
    *  In this example, we will say that the sender is the user that needs to verify that the other person is real before providing them information.   
    ```Note:  This is important detail because it affects the process.  Later, the sender will send an encrypted message to the receiver and ask them to decode it and send it back.  If the message matches the original message then their authencity has been confirmed.```
1.  First, the users choose numbers for a private key and a public key.  The private key should not be shared with anyone.  For the program written, I would choose numbers between 100 and 9,999.  Much larger numbers could be selected but this keeps the calculation steps very brief.
1.  Next, the two users must exchange public keys.  This is not sensitive information.  The expectation is that a 3rd party that is up to no good can have them and it doesn't cause an issue.
1.  Next, the sender gives a calculated "partial" key to the receiver using `Equation 1`.  
1.  The receiver decrypts the message using `Equation 3` and then encrypts it with `Equation 5` and sends this value to the sender.
1.  The sender now uses `Equation 4` to translate the 


Why do this - Time complexity of Finding Prime Roots

<br>
Notes:  Types of public/private key generation algorithms
*  **Rivest-Shamir-Adelman (RSA)** – Oldest of the public-private key cryptography systems. Frequently used to transmit shared keys for symmetric key cryptography  

*  **Digital Signature Standard (DSS)** – a Federal Information Processing Standard specifying the algorithms that can be used to generate digital signatures used by NIST  

*  **Elliptic curve cryptography (ECC)** – As its name implies, ECC relies on elliptic curves to generate keys. Often used for key agreement and digital signatures. At PreVeil, we use elliptic-curve cryptography’s Curve-25519 and NIST P-256.  

    *Source* :  <cite>https://www.preveil.com/blog/public-and-private-key/#:~:text=Public%20and%20private%20keys%20form,to%20encrypt%20and%20decrypt%20messages.</cite>  

<br>

### Generating Public and Private Keys  
*** 
The sender and receiver will need to this part.
1.  Generate two prime number: $ \ p_{1}$, $p_{2}$   
    *  i.e. 7, 11
2.  Calculate their product:  $ \ n = p_{1} * p_{2}$  
    *  i.e. n = 77
4.  Calculate Prime Factorization:  $\phi(n) = (p_{1}-1)*(p_{2} - 1)$ 
    * i.e. $\phi(n)$ = 3016
3.  Select a random value between 1 and $\phi(n)$
    *  i.e. e = 3
$$
\text{where e} = \begin{cases}
\ *&\text{small number}  \\
\ *&\text{odd number} \\
\ *&\text{not a root of } \phi(n) \\
\end{cases}
$$    

5.  Calculate the private key, $d$ :   
$$
\tag{Private Key} d = {k \phi(n) + 1 \over e}
$$
6.  { $n,e$ } make up the public key.
<br>  
<br>

### Sending/Receiving Encrypted Messages
***
7.  The sender gives the receiver these two numbers.  
8.  The receiver uses this information to encrypt their message using the senders public key { $n,e$ }:
$$
\text{encrypted message} = c_{m} = m^e \bmod n  
$$
9.  The receiver sends the encrypted message back to the sender and the message is unscrambled with the private key by solvind for $m$:
$$
m = {c_{m}}^{ed} \bmod n
$$
Theory    

5.  Prime Factorization is not easy to calculate.  The larger the number results in an exponential longer amount of time for the factorization to complete.  It can take days or even years for a computer to calculate factorizations for large numbers.  The concept of the difficulty to calculate resulting in long delays is called Time Complexity. 
5.  One Way Function Derivation:  
$$
\tag{1} m^{\phi(n)} = 1 \bmod n  
$$
$$
\tag{2} m^{k\phi(n)} = 1 \bmod n
$$
$$
\tag{3} m*m^{k\phi(n)} = m \bmod n
$$
$$
\text{simplify to} \\
m^{k \phi(n) + 1} = m \bmod n
$$
$$
\text{by equivalency} \\
m^{ed} = m \bmod n
$$
$$
\tag{4} ed = k \phi(n) + 1
$$
where d is the private key
and e is a random selected small number

6.  Calculate encryption message, $c_{m}$, using:
 $$
 \text{encrypted message} = c_{m} = m^e \bmod n  
 $$
 $$
 \begin{align*}
    where \ m& = \text{message to be encrypted} \\
            n& = 
\end{align*}
 $$

$$
 \text{dencrypted message} = m = m^{ed} \bmod n  
 $$

The Process
1.  The sender gives the receiver $ e, n $.  The two parts together make the public key.
1.  The receiver now encrypts their message, $m$ and calls it $c_{m}$:  
$$
c_{m} = m^{e} \bmod n
$$
2.  The sender can now decrypt the message by determining $m$:
$$
{m = c_{m}}^{ed} \bmod n
$$
$$
\begin{align*}
    where \ \ \ \ c_{m}& = \text{message to be decrypted} \\
                  e& = \text{sender's public key, e} \\
                  n& = \text{sender's public key, n} \\
                  d& = \text{receiver's private key}
\end{align*}
$$



Resource:  
https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/intro-to-rsa-encryption 













