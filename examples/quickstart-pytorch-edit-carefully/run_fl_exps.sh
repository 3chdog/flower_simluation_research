# ###   for test   ###
# n=3

# cnum_origin="options.num-supernodes = 10"
# cnum_list=(\
# "options.num-supernodes = 10" \
# "options.num-supernodes = 10" \
# "options.num-supernodes = 10" \
# )
# cnum_list=("${cnum_origin}" "${cnum_list[@]}")

# lr_origin="learning-rate = 0.01"
# lr_list=(\
# "learning-rate = 0.01" \
# "learning-rate = 0.01" \
# "learning-rate = 0.01" \
# )
# lr_list=("${lr_origin}" "${lr_list[@]}")

# hetero_origin="hetero = 1"
# hetero_list=(\
# "hetero = 0" \
# "hetero = 1" \
# "hetero = 1" \
# )
# hetero_list=("${hetero_origin}" "${hetero_list[@]}")
# ### for test end ###



### for real test ###
n=28

cnum_origin="options.num-supernodes = 100"
cnum_list=(\
"options.num-supernodes = 2" \
"options.num-supernodes = 6" \
"options.num-supernodes = 10" \
"options.num-supernodes = 16" \
"options.num-supernodes = 20" \
"options.num-supernodes = 50" \
"options.num-supernodes = 100" \
"options.num-supernodes = 2" \
"options.num-supernodes = 6" \
"options.num-supernodes = 10" \
"options.num-supernodes = 16" \
"options.num-supernodes = 20" \
"options.num-supernodes = 50" \
"options.num-supernodes = 100" \
"options.num-supernodes = 2" \
"options.num-supernodes = 6" \
"options.num-supernodes = 10" \
"options.num-supernodes = 16" \
"options.num-supernodes = 20" \
"options.num-supernodes = 50" \
"options.num-supernodes = 100" \
"options.num-supernodes = 2" \
"options.num-supernodes = 6" \
"options.num-supernodes = 10" \
"options.num-supernodes = 16" \
"options.num-supernodes = 20" \
"options.num-supernodes = 50" \
"options.num-supernodes = 100" \
)
cnum_list=("${cnum_origin}" "${cnum_list[@]}")

lr_origin="learning-rate = 0.001"
lr_list=(\
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.01" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
"learning-rate = 0.001" \
)
lr_list=("${lr_origin}" "${lr_list[@]}")

hetero_origin="hetero = 1"
hetero_list=(\
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 0" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
"hetero = 1" \
)
hetero_list=("${hetero_origin}" "${hetero_list[@]}")


# function with parameters: original_text, replace_text
function replace_text {
    sed -i "s/$1/$2/g" pyproject.toml
}

# search the text in the file
search_string_in_file() {
    local string="$1"
    local file="$2"

    if grep -q "$string" "$file"; then
        echo ":)) String '$string' found in $file"
        return 0
    else
        echo "X(( String '$string' not found in $file"
        return 1
    fi
}


# from 0 to n, echo the number
for i in $(seq 1 $n); do
    echo -e "\n===\n[EXPERIMENT #$i]\n"

    # check previous hyperparameters exist
    echo -e "[Checking]"
    search_string_in_file "${cnum_list[$i-1]}" pyproject.toml || exit 1
    search_string_in_file "${lr_list[$i-1]}" pyproject.toml || exit 1
    search_string_in_file "${hetero_list[$i-1]}" pyproject.toml || exit 1
    echo -e "Checking done. Successfully. Go on this experiment.\n"

    # replace the num clients
    echo -e "[Replacing Config]"
    replace_text "${cnum_list[$i-1]}" "${cnum_list[$i]}"
    echo "replace num clients: \"${cnum_list[$i-1]}\" -> \"${cnum_list[$i]}\""
    # replace the learning rate
    replace_text "${lr_list[$i-1]}" "${lr_list[$i]}"
    echo "replace learning rate: \"${lr_list[$i-1]}\" -> \"${lr_list[$i]}\""
    # replace the hetero
    replace_text "${hetero_list[$i-1]}" "${hetero_list[$i]}"
    echo "replace hetero: \"${hetero_list[$i-1]}\" -> \"${hetero_list[$i]}\""
    echo -e "\n"
    # run the experiment
    cat pyproject.toml
    flwr run .
    # end
    echo -e "\n[EXPERIMENT #$i] DONE\n===\n"
done