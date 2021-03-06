#LAURA RUBIO, DAVID OBANDO
import math
def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    lista=None
    for index in range(0,node.count(None)):
        if (index==0):
            lista=[node[:]]
        else:
            lista = lista+[node[:]]
    count =0
    count2=0
    for indexes in lista:
        changed=True
        for index in range(count,len(indexes)):
        
            if indexes[index] is None and changed:
                indexes[index]=chosen_symbol
                changed=False
                count2=index
        finded=True
        for i in range(count2,len(indexes)):
        
            if node[i]==None and finded:
                count = i+1
                finded=False
    return lista       

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol,alpha,beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node


        return (-math.inf,node) if is_maximizing_player_turn else (math.inf, node)

    children = generate_children(node, chosen_symbol)

   
    for child in children:
        eval = mini_max_ab(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol),alpha,beta)
        maxi = -math.inf
        if is_maximizing_player_turn:
            
            points = eval[0]
            nodee = eval[1]
            maxi = max(maxi,points)
            alpha = max(alpha,points)
            if beta <=alpha:
                break
            
        else: 
            
            points = eval[0]
            nodee = eval[1]
            maxi = min(maxi,points)
            beta = min(beta,points)
            if beta <=alpha:
                break
    return (maxi,child)

def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    children_results = list(map(
        lambda child: [
            mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
            child
        ],
        children
    ))

    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)