pub fn selection_sort<T: Ord>(arr: &mut [T]) {
    for i in 0..arr.len() {
        let mut smallest = i;
        for j in i..arr.len() {
            if arr[j] < arr[smallest] {
                smallest = j;
            }
        }
        arr.swap(i, smallest);
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_selection_sort() {
        let mut res = vec!["d", "a", "c", "b"];
        selection_sort(&mut res);
        assert_eq!(res, vec!["a", "b", "c", "d"]);
    }
}
