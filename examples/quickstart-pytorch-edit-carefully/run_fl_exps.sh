n=6

seeds_origin="seed = 45"
seeds_list=(\
"# seed = 42" \
"# seed = 42" \
"# seed = 42" \
"seed = 43" \
"seed = 44" \
"seed = 45" \
)
seeds_list=("${seeds_origin}" "${seeds_list[@]}")

lr_origin="learning-rate = 0.001"
lr_list=(\
"learning-rate = 0.1" \
"learning-rate = 0.01" \
"learning-rate = 0.001" \
"learning-rate = 0.1" \
"learning-rate = 0.01" \
"learning-rate = 0.001" \
)
lr_list=("${lr_origin}" "${lr_list[@]}")


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
# if the string is not found, exit
search_string_in_file "${seeds_origin}" pyproject.toml || exit 1
search_string_in_file "${lr_origin}" pyproject.toml || exit 1

# from 0 to n, echo the number
for i in $(seq 1 $n); do
    echo -e "\n===\n[EXPERIMENT #$i]\n"
    # replace the seed
    replace_text "${seeds_list[$i-1]}" "${seeds_list[$i]}"
    echo "replace seed: \"${seeds_list[$i-1]}\" -> \"${seeds_list[$i]}\""
    # replace the learning rate
    replace_text "${lr_list[$i-1]}" "${lr_list[$i]}"
    echo "replace learning rate: \"${lr_list[$i-1]}\" -> \"${lr_list[$i]}\""
    # run the experiment
    cat pyproject.toml
    flwr run .
    # end
    echo -e "\n[EXPERIMENT #$i] DONE\n===\n"
done