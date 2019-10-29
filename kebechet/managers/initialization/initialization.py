#!/usr/bin/env python3
# Kebechet
# Copyright(C) 2019 Ronan Souza
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
from kebechet.managers.manager import ManagerBase
from kebechet.utils import cloned_repo

_LOGGER = logging.getLogger(__name__)


class InitManager(ManagerBase):
    """Manager for initializing Kebechet configs"""

    def run(self) -> None:
        with cloned_repo(self.service_url, self.slug, depth=1) as repo:
            repo.git.checkout('HEAD', b="kebechet-initialization")
            repo.git.add(A=True)
            repo.index.commit("creating yaml file")
            repo.remote().push("kebechet-initialization")

            request = self.sm.open_merge_request(
                "Initializing Kebechet",
                "kebechet-initialization",
                body="Imagine a body here",
                labels=["enhancement"]
            )

            _LOGGER.info(
                f"Opened merge request with {request.number} for kebechet initialization {self.slug} "
            )





