
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int ans = n;
    for (int i = 0; i < n - 1; ++i) {
        if ((a[i] + 1) % a[i + 1] == 0 || (a[i + 1] + 1) % a[i] == 0) {
            ans = std::min(ans, n - 2);
        } else {
            ans = std::min(ans, n - 1);
            break;
        }
    }

    std::cout << ans << std::endl;

    return 0;
}
