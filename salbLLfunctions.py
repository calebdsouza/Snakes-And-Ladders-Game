"""
# Copyright Caleb, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode


def salb2salbLL(salb):
    """
    (SALboard) -> Linked List
    Returns a linked list representation of a gievn Snakes and Ladders borad of
    a given snakes and ladders board represent by a dictionanry.
    REQ: The number of squares of the given SALboard must > 0
    REQ: The dicitoanry of snakes cannot be empty
    """
    # Get the number of squares in the given dictionary representation
    number_of_squares = salb.numSquares
    # Create an empty salbLL without any snadders
    head = creat_empty_salbLL(number_of_squares)

    # Get a dictionary of sandders from the dictionary representation of
    # SALboard
    snadders_dict = salb.snadders
    # Populate the created linked list of SALBnodes with sandders
    populate_with_sanders(head, snadders_dict)

    # Return the created SALB circular linked list
    return head


def willfinish(first, stepsize):
    """
    (SALBnode, int) -> bool
    Given a circular linked list of SALBnodes(salbLL) and a step-size, will
    reutrn true if the step-size would reuslt in the tracker landing on the
    last SALBnode of the given salbLL, otherwise, returns false if it never
    lands on the last SALBnode.
    REQ: There must be alteast more than one SALBnode in the given salbLL
    >>> snadder_dict = {4:3}
    >>> square_num = 5
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> stepsize = 1
    >>> willfinish(salb_ll, stepsize)
    False
    >>> snadder_dict = {4:3, 6:7, 8:9}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> stepsize = 7
    >>> willfinish(salb_ll, stepsize)
    True
    >>> snadder_dict = {4:3, 6:7, 8:9}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> stepsize = 2
    >>> willfinish(salb_ll, stepsize)
    False
    >>> snadder_dict = {4:5, 7:3}
    >>> square_num = 9
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> stepsize = 3
    >>> willfinish(salb_ll, stepsize)
    True
    """
    # Create a place to store the result of wheather the given salbLL and
    # Stepsize will finsih
    will_finish = False
    # Create check to state if it has been determined if the given salbLL and
    # stepsize will finish or not
    is_determined = False

    # Create a pointer which moves through each SALBnode in the given salbLL
    # according to the given step size
    stepsize_pointer = move_stepsize(first, stepsize - 1, first)
    # Create a pointer which moves through each SALBnode in teh given salbLL by
    # two times the given step size
    double_stepsize_pointer = move_stepsize(first, stepsize - 1, first)
    # Continue to move the both pointers of the two differnce stepsizes until
    # it has determined the given step size will land on the last SALBnode
    while(not is_determined):
        # Move the double stepsize pointer over
        stepsize_pointer = move_stepsize(first, stepsize, stepsize_pointer)
        # Move the regular stepsze pointer over
        double_stepsize_pointer = move_stepsize(first, stepsize,
                                                double_stepsize_pointer)
        # Check if the double_step_pointer is on the last SALBnode of the given
        # salbLL
        if(double_stepsize_pointer.next != first):
            # Move the double_step_pointer over
            double_stepsize_pointer = move_stepsize(first, stepsize,
                                                    double_stepsize_pointer)
        else:
            # The given stepsize will allow the relgular pointer to land on the
            # last SALBnode in the given salbLL
            will_finish = True
            # It has been determined that the stepsize will finish
            is_determined = True
        # Check if the current regular stepsize_pointer is on the same SALBnode
        # as the double_stepsize_pointer
        if stepsize_pointer == double_stepsize_pointer:
            # It has been determined that the stepsize will finish
            is_determined = True

    # Return the reuslt of wheather the stepsize will finish
    return will_finish


def whowins(first, step1, step2):
    """
    (SALBnode, int, int) -> int
    Given a cirular linked list of SALBnodes (salbLL) and two step sizes,
    returns a 1 if the step1 wins, by landing on the last square in the given
    salbLL before step2, otherwise, returens 2 if the step2 stepsize wins.
    REQ: One of the two given step size must be able to finsih the given salbLL
    by landing on it's last SALBnode
    REQ: The given step size, step1 and step2, must be greater than 0
    REQ: The given salbLL, first, must have more than one SALBnode
    REQ: step1 cannot be equal to step2
    >>> snadder_dict = {4:3, 6:7, 8:9}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> step1 = 2
    >>> step2 = 7
    >>> whowins(salb_ll, step1, step2)
    2
    >>> snadder_dict = {2:5}
    >>> square_num = 6
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> step1 = 1
    >>> step2 = 2
    >>> whowins(salb_ll, step1, step2)
    1
    >>> snadder_dict = {2:5, 11:7, 9:12}
    >>> square_num = 13
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> step1 = 3
    >>> step2 = 2
    >>> whowins(salb_ll, step1, step2)
    1
    """
    # Create a place to store the winner
    winner = 0
    # Determine if the first given stepsize, step1, will finsih
    will_step1_finish = willfinish(first, step1)
    # Determine if the second given stepsize, step2, will finish
    will_step2_finish = willfinish(first, step2)

    # Check which of the two given step sizes or if both will finish
    if(will_step1_finish and will_step2_finish):
        # Create a place to track if player1 using step1 is the winner
        is_player1_winner = False
        # Create a place to trak if player2 using step2 is the winner
        is_player2_winner = False
        # Place the fist player on the given board(salbLL)
        player_1 = find_SALBnode(first, step1)
        # Place the sevond player on the given board(salbLL)
        player_2 = find_SALBnode(first, step2)

        # Continue to move player1 and player2 until one of the players lands
        # on the last SALBnode in the given salbLL
        while((not is_player1_winner) and (not is_player2_winner)):
            # Check if the player1 or player 2 landed on the last SALBnode of
            # the given salbLL first
            if((player_1.next != first) and (player_2.next != first)):
                # Move player1 from it's current position over, step1 SALBnodes
                player_1 = move_stepsize(first, step1, player_1)
                # Move player2 from it's current position over, step2 SALBnodes
                player_2 = move_stepsize(first, step2, player_2)
            elif(player_1.next == first):
                # Set player 1 as the winner
                is_player1_winner = True
            else:
                # Set player 2 as the winner
                is_player2_winner = True
        if(is_player1_winner):
            # Set winner is player 1
            winner = 1
        else:
            # Set winner is player 2
            winner = 2
    elif(not will_step1_finish):
        # Set the winner to be the second given step size, step2
        winner = 2
    else:
        # Set the winner to be the first given step size, step1
        winner = 1

    # Return the resultant winner
    return winner


def dualboard(first):
    """
    (SALBnode) -> SALBnode
    Givena linked list representation of an SALboard, returns the linked list
    representation of it's dual, where the number of squares remains the same,
    but the source SALBnodes are interchanged with the destination SALBnodes.
    REQ: The given linked list representation of cannot have the nth
    SALBnode(the last node in the linked list) be a source or destination node
    REQ: No square(SALBnode) can be the destination for more than one snadder
    REQ: No sqaure(SALBnode) can be the source for more than one snadder
    """
    # Get the number of SALBnodes in the given linked list of SALBnodes(salbLL)
    count = count_SALBnodes(first)
    # Create an emppty salbLL without any snsadders
    new_salbLL = creat_empty_salbLL(count)
    # Create a point to track the current position of the SALBnode in the given
    # salbLL
    current = first
    # Loop through the given salbLL
    while(current.next != first):
        # Check if the current SALBnode is a soruce of a snadder
        if(current.snadder is not None):
            # Store the current SALBnode as the source of the sandder
            source = current
            # Store the sandder pointer as the destination of this sandder
            destination = current.snadder
            # Get the position index of the source SALBnode
            source_position_index = get_SALBnode_position(first, source)
            # Get the position index of the destination SALBnode
            destination_position_index = get_SALBnode_position(first,
                                                               destination)
            # Find the source SALBnode in the copy of the given salbLL and
            # set it to be the destinaton of the dualboard
            copy_source = find_SALBnode(new_salbLL, destination_position_index)
            # Find the destination SALBnode in the copy of the given salbLL and
            # set it to be the source of the dualboard
            copy_destination = find_SALBnode(new_salbLL, source_position_index)
            # Set the copy destination as the the destination for the copy
            # source, creating a snadder in the copy salbLL
            copy_source.snadder = copy_destination
        # Move to the next SALBnode in the given linked list
        current = current.next
    # Return the result new salbLL copy of the given salbLL
    return new_salbLL


# HELPER FUNCTIONS
def creat_empty_salbLL(number_of_squares):
    """
    (SALBnode) -> SALBnode
    Given the head pointer, which point to the head of a SALBoard linked list
    will createan empty SALBoard linked list, without any snadders.
    REQ: The given head linked list must contain at least one SALBnode
    >>> number_of_squares = 10
    >>> empty_LL = creat_empty_salbLL(number_of_squares)
    >>> count = count_SALBnodes(empty_LL)
    >>> count == number_of_squares
    True
    """
    # Create a point which points to the current head of the linked list
    tail = SALBnode()
    # Create a pointer which points to the current tail of the linked list
    head = tail
    # Add a numebr of SALBnodes equal to the numer of sqaure in the given
    # dictionary representation
    for square_index in range(1, number_of_squares):
        # Add one SALBNode to the head linked list
        head = SALBnode(head)
    # Link the tail node of the created linked list to the head node thorugh
    # the next point of the tail node
    tail.next = head
    # Return the empty salbLL
    return head


def populate_with_sanders(head, snadder_dict):
    """
    (SALBnode) -> NoneType
    Given a head pointer which point to a linked list of SALBnodes and a
    dicitonary of sandders, where each key is the source SALBnode and the
    value is the destination SALBnode, will create links between the source
    SALBnode and the destination SALBnode.
    REQ: The given dictionary of snadders cannot have the nth SALBnode(the
    last node in the linked list)be a source ordestination node
    REQ: No square can be the destination for more than one snadder
    REQ: A dictionary data structure will not alow a sqaure to be the source
    for more than one sandder
    REQ: Dictionary should not be empty
    >>> snadder_dict = {3:4, 8:5}
    >>> number_of_squares = 10
    >>> ll = creat_empty_salbLL(number_of_squares)
    >>> populate_with_sanders(ll, snadder_dict)
    >>> node = find_SALBnode(ll, 3)
    >>> position = get_SALBnode_position(ll, node.snadder)
    >>> position == 4
    True
    >>> node = find_SALBnode(ll, 8)
    >>> position = get_SALBnode_position(ll, node.snadder)
    >>> position == 5
    True
    """
    # Get a list keys fromt the given dicitonary of snadders
    keys_list = list(snadder_dict.keys())

    # Loop through each key value
    for key in keys_list:
        # Find the source SALBnode in the given Linked List of SALBnodes
        source = find_SALBnode(head, key)
        # Get the poititon of the destination SALBnode
        destination_position = int(snadder_dict[key])
        # Find the destination SALBnode in the given Linked List of SALBnodes
        destination = find_SALBnode(head, destination_position)
        # Point the source node to the destination node
        source.snadder = destination


def find_SALBnode(head, square_number):
    """
    (SALBnode, int) -> SALBnode
    Given a circular linked list of SALBnodes, with 'head' pointing to the
    first SALBnode in the circular linked list, and the SALBnode return the
    SALBnode at the poition eqaual to the given square number.
    REQ: head must point to at least one SALBnode
    REQ: the squre_number < the number of SABLnodes in the circular linked list
    that the given head points to.
    >>> number_of_squares = 10
    >>> ll = creat_empty_salbLL(number_of_squares)
    >>> node = find_SALBnode(ll, 5)
    >>> get_SALBnode_position(ll, node)
    5
    """
    # Create a coutner to keep track of the current square number
    square_count = 1
    # Create a pointer that points to the first node in the give circular
    # linked list
    first_SALBnode = head
    # Create a pointer to keep track of the position of the current SALBnode
    current = first_SALBnode
    # Move the current pointer down to the next SALBnode n time where n =
    # square_numebr
    while(current.next != first_SALBnode and square_count != square_number):
        # Move to the next SALBnode
        current = current.next
        # Increase the square number to match the current square poition
        square_count += 1

    # Return the resultant current SALBnode which is in the n poisiton where n
    # equals the given sqare_number
    return current


def count_SALBnodes(head):
    """
    (SALBnode) -> int
    Given a linked list of SALBnodes(salbLL), will count the total number of
    SALBnode in the given salbLL and return the final count.
    REQ: The given salbLL must have at least one SALBnode
    >>> snadder_dict = {3:4, 6:7}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> count = count_SALBnodes(salb_ll)
    >>> count == square_num
    True
    """
    # Set the count to 1 since we will start at the count at the seond node
    count = 1
    # Creat a pointer to keep track of the position of the current SALBnode
    current = head
    # Loop through each node in the given salbLL
    while(current.next != head):
        # Move to the next SALBnode in the given salbLL
        current = current.next
        # Increment the count by 1
        count += 1
    # Return the final count
    return count


def get_SALBnode_position(head, node):
    """
    (SALBnode, SALBnode) -> int
    Given an SALBnode circlar linkded list(salbLL), and a SALBnode to look for
    in the given linkde list, get the position index of the given SALBnode to
    look for and return the int representation of that position index.
    REQ: The given SLABnode must be in the given salbLL
    >>> snadder_dict = {3:4, 6:7}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> position = 5
    >>> node = find_SALBnode(salb_ll, position)
    >>> found_position = get_SALBnode_position(salb_ll, node)
    >>> position == found_position
    True
    >>> snadder_dict = {3:4, 6:7}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> position = 1
    >>> node = find_SALBnode(salb_ll, position)
    >>> found_position = get_SALBnode_position(salb_ll, node)
    >>> position == found_position
    True
    >>> snadder_dict = {3:4, 6:7}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> position = 10
    >>> node = find_SALBnode(salb_ll, position)
    >>> found_position = get_SALBnode_position(salb_ll, node)
    >>> position == found_position
    True
    """
    # Create a place to store the position index of the given SLABndoe
    position_index = 1
    # Create a pointer to track the current poistion of the current SALBnode
    current = head
    # Loop through the given salbLL to find the given SLABndoe
    while(current.next != head and current != node):
        # Move to the next SALBnode in the given salbLL
        current = current.next
        # Increment the position index to match the current SALBnode position
        position_index += 1
    # Return the resulatant psoition index
    return position_index


def move_stepsize(head, stepsize, current):
    """
    (SALBnode, int, SALBnode) -> NoneType
    Given a circular linked list of SALBnoes (salbLL), a fixed setpsize to
    move the given pointer of the current SALBnode will move the given pointer
    over n number of SLABnode where n is equal to the stepsize.
    REQ: The given salbLL must have atleast two SALBnodes
    >>> number_of_squares = 10
    >>> ll = creat_empty_salbLL(number_of_squares)
    >>> current = ll
    >>> stepsize = 2
    >>> current = move_stepsize(ll, stepsize, current)
    >>> get_SALBnode_position(ll, current)
    3
    >>> snadder_dict = {3:5, 6:7}
    >>> square_num = 10
    >>> salb_dict = SALboard(square_num, snadder_dict)
    >>> salb_ll = salb2salbLL(salb_dict)
    >>> current = salb_ll
    >>> stepsize = 2
    >>> current = move_stepsize(salb_ll, stepsize, current)
    >>> get_SALBnode_position(salb_ll, current)
    5
    """
    # Given the step size move the given current pointer over that many
    # SALBnodes
    for step in range(stepsize):
        # Move the current pointer to the next SALBndoe
        current = current.next
    # Check of the current SALBnode is the source of a snadder
    if(current.snadder is not None):
        # Set teh current pointer to the destination of this snadder
        current = current.snadder
    # Return the new position
    return current
