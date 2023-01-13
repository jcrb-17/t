export default function format2(n) {
    n = parseInt(n);
    if (n == 1) {
        return 0;
    } else {
        return (n * 10) - 10;
    }
}