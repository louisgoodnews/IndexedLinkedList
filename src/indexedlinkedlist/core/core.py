"""
Author: Louis Goodnews
Date: 2025-09-21
"""

from typing import Any, Final, Iterator, Optional, Self, Union
from uuid import UUID, uuid4


from utils.utils import invert_dict

__all__: Final[list[str]] = ["IndexedLinkedList"]


class IndexedLinkedNode:
    """
    IndexedLinkedNode class for representing a node in an indexed linked list.
    """

    def __init__(
        self,
        identifier: UUID,
        value: Any,
    ) -> None:
        """
        Initialize the IndexedLinkedNode with the passed identifier and value.

        Args:
            identifier (UUID): The identifier of the node.
            value (Any): The value of the node.

        Returns:
            None
        """

        # Store the passed identifier UUID in an instance variable
        self._identifier: UUID = identifier

        # Store the passed value in an instance variable
        self._value: Any = value

    def __contains__(
        self,
        key: Any,
    ) -> bool:
        """
        Check if the value of this node contains the passed key.

        Args:
            key (Any): The key to check.

        Returns:
            bool: True if the value of this node contains the passed key, False otherwise.
        """

        # Check, if the value of this node is None
        if self._value is None:
            # Return False
            return False

        # Return True, if the value of this node contains the passed key
        return key in self._value

    def __eq__(
        self,
        other: "IndexedLinkedNode",
    ) -> bool:
        """
        Check if this node is equal to the passed node.

        Args:
            other (IndexedLinkedNode): The node to compare with.

        Returns:
            bool: True if this node is equal to the passed node, False otherwise.
        """

        # Check, if the passed object is an instance of IndexedLinkedNode
        if not isinstance(
            other,
            IndexedLinkedNode,
        ):
            # Return False
            return False

        # Return True, if the identifiers of this node and the passed node are equal
        return self._identifier == other._identifier

    def __getitem__(
        self,
        key: str,
    ) -> Any:
        """
        Get the value of the passed key.

        Args:
            key (str): The key to get the value of.

        Returns:
            Any: The value of the passed key.
        """

        return self.__dict__[key]

    def __repr__(self) -> str:
        """
        Get the string representation of this node.

        Returns:
            str: The string representation of this node.
        """

        return f"<{self.__class__.__name__}(identifier={self._identifier}, value={self._value})>"

    def __setitem__(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Set the value of the passed key.

        Args:
            key (str): The key to set the value of.
            value (Any): The value to set.

        Raises:
            AttributeError: If the passed key is not "value".
        """

        # Check, if the passed key is not "value"
        if key.lower() != "value":
            # Raise an AttributeError
            raise AttributeError(
                f"Attribute '{key}' of {self.__class__.__name__} is immutable."
            )

        # Update the value with the passed value
        self.__dict__[key] = value

    def __str__(self) -> str:
        """
        Get the string representation of this node.

        Returns:
            str: The string representation of this node.
        """

        return str(self._value)

    @property
    def identifier(self) -> UUID:
        """
        Get the identifier of this node.

        Returns:
            UUID: The identifier of this node.
        """

        # Return the identifier of this node
        return self._identifier

    @property
    def value(self) -> Any:
        """
        Get the value of this node.

        Returns:
            Any: The value of this node.
        """

        # Return the value of this node
        return self._value

    @value.setter
    def value(
        self,
        value: Any,
    ) -> None:
        """
        Set the value of this node.

        Args:
            value (Any): The value to set.
        """

        # Update the value with the passed value
        self._value = value

    def clone(self) -> "IndexedLinkedNode":
        """
        Create a clone of this node.

        Returns:
            IndexedLinkedNode: A clone of this node.
        """

        # Create and return a new instance of the IndexedLinkedNode
        return IndexedLinkedNode(
            identifier=self._identifier,
            value=self._value,
        )

    def copy(self) -> "IndexedLinkedNode":
        """
        Create a copy of this node.

        Returns:
            IndexedLinkedNode: A copy of this node.
        """

        # Create and return a new instance of the IndexedLinkedNode
        return IndexedLinkedNode(
            identifier=uuid4(),
            value=self._value,
        )


class IndexedLinkedNodeFactory:
    """
    Factory class for creating IndexedLinkedNode instances.
    """

    @classmethod
    def create(
        cls,
        identifier: UUID,
        value: Any,
    ) -> IndexedLinkedNode:
        """
        Create a new IndexedLinkedNode instance.

        Args:
            identifier (UUID): The identifier of the node.
            value (Any): The value of the node.

        Returns:
            IndexedLinkedNode: A new IndexedLinkedNode instance.
        """

        # Create and return a new instance of the IndexedLinkedNode
        return IndexedLinkedNode(
            identifier=identifier,
            value=value,
        )

    @classmethod
    def create_default(
        cls,
        value: Optional[Any] = None,
    ) -> IndexedLinkedNode:
        """
        Create a default IndexedLinkedNode instance.

        Args:
            value (Optional[Any]): The value of the node.

        Returns:
            IndexedLinkedNode: A default IndexedLinkedNode instance.
        """

        # Create and return a new instance of the IndexedLinkedNode
        return IndexedLinkedNode(
            identifier=uuid4(),
            value=value,
        )


class IndexedLinkedNodeBuilder:
    """
    Builder class for creating IndexedLinkedNode instances.
    """

    def __init__(self) -> None:
        """
        Initialize the IndexedLinkedNodeBuilder with an empty configuration.

        Returns:
            None
        """

        # Initialize the configuration with an empty dictionary
        self._configuration: dict[str, Any] = {}

    def __eq__(
        self,
        other: "IndexedLinkedNodeBuilder",
    ) -> bool:
        """
        Check if this builder is equal to the passed builder.

        Args:
            other (IndexedLinkedNodeBuilder): The builder to compare with.

        Returns:
            bool: True if this builder is equal to the passed builder, False otherwise.
        """

        # Check, if the passed object is an instance of IndexedLinkedNodeBuilder
        if not isinstance(
            other,
            IndexedLinkedNodeBuilder,
        ):
            # Return False
            return False

        # Return True, if the configurations of this builder and the passed builder are equal
        return self._configuration == other.configuration

    def __getitem__(
        self,
        key: str,
    ) -> Any:
        """
        Get the value of the passed key.

        Args:
            key (str): The key to get the value of.

        Returns:
            Any: The value of the passed key.
        """

        # Return the value of the passed key
        return self._configuration[key]

    def __len__(self) -> int:
        """
        Get the number of key-value pairs in the configuration.

        Returns:
            int: The number of key-value pairs in the configuration.
        """

        # Return the number of key-value pairs in the configuration
        return len(self._configuration)

    def __repr__(self) -> str:
        """
        Get the string representation of this builder.

        Returns:
            str: The string representation of this builder.
        """

        return f"<{self.__class__.__name__}(configuration={self._configuration})>"

    def __setitem__(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Set the value of the passed key.

        Args:
            key (str): The key to set the value of.
            value (Any): The value to set.
        """

        # Set the value of the passed key
        self._configuration[key] = value

    def __str__(self) -> str:
        """
        Get the string representation of this builder.

        Returns:
            str: The string representation of this builder.
        """

        return str(self._configuration)

    @property
    def configuration(self) -> dict[str, Any]:
        """
        Get the configuration of this builder.

        Returns:
            dict[str, Any]: The configuration of this builder.
        """

        # Return the configuration of this builder
        return dict(self._configuration)

    def build(self) -> IndexedLinkedNode:
        """
        Build an IndexedLinkedNode instance from the configuration.

        Returns:
            IndexedLinkedNode: An IndexedLinkedNode instance built from the configuration.
        """

        # Return the IndexedLinkedNode instance
        return IndexedLinkedNodeFactory.create(**self._configuration)

    def build_default(self) -> IndexedLinkedNode:
        """
        Build a default IndexedLinkedNode instance from the configuration.

        The IndexedLinkedNode instance is built using the factory's default constructor.
        In this case a value argument is not required in order for the factory to create a default instance.

        Returns:
            IndexedLinkedNode: A default IndexedLinkedNode instance built from the configuration.
        """

        # Return the default IndexedLinkedNode instance
        return IndexedLinkedNodeFactory.create_default(
            value=self._configuration.get(
                "value",
                None,
            )
        )

    def with_identifier(
        self,
        value: Optional[UUID] = None,
    ) -> Self:
        """
        Set the identifier of the node.

        Args:
            value (Optional[UUID]): The identifier to set.

        Returns:
            Self: The builder instance.
        """

        # Check, if the identifier is already set
        if "identifier" in self._configuration:
            # Return the builder instance
            return self

        # Check, if the passed identifier value is None
        if value is None:
            # Set the identifier to a random UUID
            value = uuid4()

        # Set the identifier
        self._configuration["identifier"] = value

        # Return the builder instance
        return self

    def with_value(
        self,
        value: Optional[Any] = None,
    ) -> Self:
        """
        Set the value of the node.

        Args:
            value (Optional[Any]): The value to set.

        Returns:
            Self: The builder instance.
        """

        # Set the value
        self._configuration["value"] = value

        # Return the builder instance
        return self


class IndexedLinkedNodeStorage:
    """
    Storage class for IndexedLinkedNode instances.
    """

    def __init__(self) -> None:
        """
        Initialize the IndexedLinkedNodeStorage with an empty storage.

        Returns:
            None
        """

        # Initialize the head node of the storage to None
        self._head: Optional[IndexedLinkedNode] = None

        # Initialize the index to uuid mapping with an empty mapping
        self._index_to_uuid: dict[int, UUID] = {}

        # Initialize the tail node of the storage to None
        self._tail: Optional[IndexedLinkedNode] = None

        # Initialize the uuid to node mapping with an empty mapping
        self._uuid_to_node: dict[UUID, IndexedLinkedNode] = {}

    def __getitem__(
        self,
        key: Union[int, UUID],
    ) -> IndexedLinkedNode:
        """
        Get the node at the passed index or identifier.

        Args:
            key (Union[int, UUID]): The index or identifier of the node to get.

        Returns:
            IndexedLinkedNode: The node at the passed index or identifier.
        """

        # Check, if the passed key is an integer
        if isinstance(
            key,
            int,
        ):
            # Return the node at the passed index
            return self._uuid_to_node[self._index_to_uuid[key]]

        # Return the node at the passed identifier
        return self._uuid_to_node[key]

    def __iter__(self) -> Iterator[IndexedLinkedNode]:
        """
        Iterate over the nodes in the storage.

        Yields:
            IndexedLinkedNode: The next node in the storage.
        """

        # Iterate over the nodes in the storage
        for node in self._uuid_to_node.values():
            # Yield the node
            yield node

    def __len__(self) -> int:
        """
        Get the size of the storage.

        Returns:
            int: The size of the storage.
        """

        # Return the size of the storage
        return len(self._index_to_uuid)

    def __repr__(self) -> str:
        """
        Get the string representation of the storage.

        Returns:
            str: The string representation of the storage.
        """

        # Return the string representation of the storage
        return f"<{self.__class__.__name__}(head={self._head}, index_to_uuid={len(self._index_to_uuid)}, size={self.size}, tail={self._tail}, unused_indices={self.unused_indices}, used_indices={self.used_indices}, uuid_to_node={len(self._uuid_to_node)})>"

    def __setitem__(
        self,
        key: Union[int, UUID],
        value: IndexedLinkedNode,
    ) -> None:
        """
        Set the node at the passed index or identifier.

        Args:
            key (Union[int, UUID]): The index or identifier of the node to set.
            value (IndexedLinkedNode): The node to set.
        """

        # Check, if the passed key is an integer
        if isinstance(
            key,
            int,
        ):
            # Set the node at the passed index
            self._uuid_to_node[self._index_to_uuid[key]] = value

        # Set the node at the passed identifier
        self._uuid_to_node[key] = value

    def __str__(self) -> str:
        """
        Get the string representation of the storage.

        Returns:
            str: The string representation of the storage.
        """

        # Return the string representation of the storage
        return self.__repr__()

    @property
    def head(self) -> Optional[IndexedLinkedNode]:
        """
        Get the head node of the storage.

        Returns:
            Optional[IndexedLinkedNode]: The head node of the storage.
        """

        # Return the head node
        return self._head

    @head.setter
    def head(
        self,
        value: IndexedLinkedNode,
    ) -> None:
        """
        Set the head node of the storage.

        Args:
            value (IndexedLinkedNode): The head node to set.
        """

        # Set the head node
        self._head = value

    @property
    def index_to_uuid(self) -> dict[int, UUID]:
        """
        Get the index to uuid mapping.

        Returns:
            dict[int, UUID]: The index to uuid mapping.
        """

        # Return the index to uuid mapping
        return dict(self._index_to_uuid)

    @property
    def size(self) -> int:
        """
        Get the size of the storage.

        Returns:
            int: The size of the storage.
        """

        # Return the size of the storage
        return self.get_size()

    @property
    def tail(self) -> Optional[IndexedLinkedNode]:
        """
        Get the tail node of the storage.

        Returns:
            Optional[IndexedLinkedNode]: The tail node of the storage.
        """

        # Return the tail node
        return self._tail

    @tail.setter
    def tail(
        self,
        value: IndexedLinkedNode,
    ) -> None:
        """
        Set the tail node of the storage.

        Args:
            value (IndexedLinkedNode): The tail node to set.
        """

        # Set the tail node
        self._tail = value

    @property
    def unused_indices(self) -> list[int]:
        """
        Get the unused indices.

        Returns:
            list[int]: The unused indices.
        """

        # Return the unused indices
        return self.get_unused_indices()

    @property
    def used_indices(self) -> list[int]:
        """
        Get the used indices.

        Returns:
            list[int]: The used indices.
        """

        # Return the used indices
        return self.get_used_indices()

    @property
    def uuid_to_node(self) -> dict[UUID, IndexedLinkedNode]:
        """
        Get the uuid to node mapping.

        Returns:
            dict[UUID, IndexedLinkedNode]: The uuid to node mapping.
        """

        # Return the uuid to node mapping
        return dict(self._uuid_to_node)

    def empty(self) -> bool:
        """
        Check, if the storage is empty.

        Returns:
            bool: True, if the storage is empty, False otherwise.
        """

        # Check, if the storage is empty
        return len(self._index_to_uuid) == 0 and len(self._uuid_to_node) == 0

    def get_available_index(self) -> int:
        """
        Get the next available index.

        Returns:
            int: The next available index.
        """

        # Iterate over the indices in the index to uuid mapping
        for index in self._index_to_uuid:
            # Check, if the index is already used
            if self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Return the index
            return index

        # Return the next available index -> being at the end of the storage
        return self.get_size()

    def get_first_unused_index(self) -> Optional[int]:
        """
        Get the first unused index.

        Returns:
            Optional[int]: The first unused index or None if none are found.
        """

        # Check, if the size of the storage is 0, i.e. the storage is empty
        if self.get_size() == 0:
            # Return None early
            return None

        # Iterate over the indices in the index to uuid mapping
        for index in self._index_to_uuid.keys():
            # Check, if the index is used
            if self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Return the index
            return index

        # Return None if no unused index is found
        return None

    def get_first_used_index(self) -> Optional[int]:
        """
        Get the first used index.

        Returns:
            Optional[int]: The first used index or None if none are found.
        """

        # Check, if the size of the storage is 0, i.e. the storage is empty
        if self.get_size() == 0:
            # Return None early
            return None

        # Iterate over the indices in the index to uuid mapping
        for index in self._index_to_uuid.keys():
            # Check, if the index is not used
            if not self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Return the index
            return index

        # Return None if no unused index is found
        return None

    def get_index_of_node(
        self,
        node: IndexedLinkedNode,
    ) -> Optional[int]:
        """
        Get the index of a node.

        Args:
            node (IndexedLinkedNode): The node to get the index of.

        Returns:
            Optional[int]: The index of the node or None if the node is not in the storage.
        """

        # Check, if the node is in the uuid to node mapping
        if node.identifier not in self._uuid_to_node:
            # Return None early
            return None

        # Return the index of the node
        return invert_dict(dictionary=self._index_to_uuid)[node.identifier]

    def get_last_unused_index(self) -> Optional[int]:
        """
        Get the last unused index.

        Returns:
            Optional[int]: The last unused index or None if none are found.
        """

        # Check, if the size of the storage is 0, i.e. the storage is empty
        if self.get_size() == 0:
            # Return None early
            return None

        # Iterate over the indices in the index to uuid mapping in reverse
        for index in reversed(self._index_to_uuid.keys()):
            # Check, if the index is used
            if self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Return the index
            return index

        # Return None if no unused index is found
        return None

    def get_last_used_index(self) -> Optional[int]:
        """
        Get the last used index.

        Returns:
            Optional[int]: The last used index or None if none are found.
        """

        # Check, if the size of the storage is 0, i.e. the storage is empty
        if self.get_size() == 0:
            # Return None early
            return None

        # Iterate over the indices in the index to uuid mapping in reverse
        for index in reversed(self._index_to_uuid.keys()):
            # Check, if the index is not used
            if not self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Return the index
            return index

        # Return None if no unused index is found
        return None

    def get_next_index(
        self,
        index: int,
    ) -> Optional[tuple[int, UUID]]:
        """
        Get the next index.

        Args:
            index (int): The index to get the next index of.

        Returns:
            Optional[tuple[int, UUID]]: The next index and the uuid of the node at the next index.
        """

        # Check, if the index is the last index
        if index == self.get_size():
            # Return None
            return None

        # Get the next index
        new_index: int = index + 1

        # Return the next index and the uuid of the node at the next index
        return (
            new_index,
            self._index_to_uuid[new_index],
        )

    def get_node_for_index(
        self,
        index: int,
    ) -> Optional[IndexedLinkedNode]:
        """
        Get the node for the passed index.

        Args:
            index (int): The index to get the node for.

        Returns:
            Optional[IndexedLinkedNode]: The node for the passed index.
        """

        # Check, if the index is in the index to uuid mapping
        if not self.has_index(index=index):
            # Return None, if the index is not in the index to uuid mapping
            return None

        # Get the uuid of the node at the index
        uuid: Optional[UUID] = self._index_to_uuid.get(
            index,
            None,
        )

        # Check, if the uuid is None
        if uuid is None:
            # Return None, if the uuid is None
            return None

        # Return the node for the uuid
        return self._uuid_to_node.get(
            uuid,
            None,
        )

    def get_node_with_value(
        self,
        value: Any,
    ) -> Optional[IndexedLinkedNode]:
        """
        Get the node with the passed value.

        Args:
            value (Any): The value to get the node with.

        Returns:
            Optional[IndexedLinkedNode]: The node with the passed value.
        """

        # Return the node with the passed value
        return next(
            (node for node in self._uuid_to_node.values() if node.value == value),
            None,
        )

    def get_previous_index(
        self,
        index: int,
    ) -> Optional[tuple[int, UUID]]:
        """
        Get the previous index.

        Args:
            index (int): The index to get the previous index of.

        Returns:
            Optional[tuple[int, UUID]]: The previous index and the uuid of the node at the previous index.
        """

        # Check, if the index is a string
        if isinstance(
            index,
            str,
        ):
            # Convert the index to an integer
            index = int(index)

        # Check, if the index is the first index
        if index == 0:
            # Return None, if the index is the first index
            return None

        # Get the previous index
        new_index: int = index - 1

        # Return the previous index and the uuid of the node at the previous index
        return (
            new_index,
            self._index_to_uuid[new_index],
        )

    def get_size(self) -> int:
        """
        Get the size of the storage.

        Returns:
            int: The size of the storage.
        """

        # Return the size of the storage
        return len(self._index_to_uuid)

    def get_used_indices(self) -> list[int]:
        """
        Get the used indices.

        Returns:
            list[int]: The used indices.
        """

        # Initialize the result list
        result: list[int] = []

        # Check, if the storage is empty
        if self.get_size() == 0:
            # Return the result list
            return result

        # Iterate over the indices in the index to uuid mapping
        for index in self._index_to_uuid:
            # Check, if the index is not used
            if not self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Append the index to the result list
            result.append(index)

        # Return the result list
        return result

    def get_unused_indices(self) -> list[int]:
        """
        Get the unused indices.

        Returns:
            list[int]: The unused indices.
        """

        # Initialize the result list
        result: list[int] = []

        # Check, if the storage is empty
        if self.get_size() == 0:
            # Return the result list
            return result

        # Iterate over the indices in the index to uuid mapping
        for index in self._index_to_uuid:
            # Check, if the index is used
            if self._index_to_uuid.get(
                index,
                None,
            ):
                # Skip the index
                continue

            # Append the index to the result list
            result.append(index)

        # Return the result list
        return result

    def has_index(
        self,
        index: int,
    ) -> bool:
        """
        Check, if the passed index is in the storage.

        Args:
            index (int): The index to check.

        Returns:
            bool: True, if the passed index is in the storage, False otherwise.
        """

        # Check, if the index is in the index to uuid mapping
        return index in self._index_to_uuid

    def has_uuid(
        self,
        uuid: UUID,
    ) -> bool:
        """
        Check, if the passed uuid is in the storage.

        Args:
            uuid (UUID): The uuid to check.

        Returns:
            bool: True, if the passed uuid is in the storage, False otherwise.
        """

        # Check, if the uuid is in the uuid to node mapping
        return uuid in self._uuid_to_node

    def has_value(
        self,
        value: Any,
    ) -> bool:
        """
        Check, if the passed value is in the storage.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True, if the passed value is in the storage, False otherwise.
        """

        # Check, if the storage is empty
        if self.get_size() == 0:
            # Return False
            return False

        # Check, if the value is in the storage
        return value in [node.value for node in self.get_nodes()]

    def get_nodes(self) -> list[IndexedLinkedNode]:
        """
        Get the nodes in the storage.

        Returns:
            list[IndexedLinkedNode]: The nodes in the storage.
        """

        # Return the nodes in the storage
        return list(self._uuid_to_node.values())

    def register(
        self,
        node: IndexedLinkedNode,
    ) -> int:
        """
        Register a node in the storage.

        Args:
            node (IndexedLinkedNode): The node to register.

        Returns:
            int: The index of the registered node.
        """

        # Register the node in the uuid to node mapping
        self._uuid_to_node[node.identifier] = node

        # Get the available index
        index: int = self.get_available_index()

        # Register the index in the index to uuid mapping
        self._index_to_uuid[index] = node.identifier

        # Check, if the index is the first index
        if index == 0:
            # Set the head to the node
            self._head = node

        # Check, if the index is the last index
        if index == self.get_size() - 1:
            # Set the tail to the node
            self._tail = node

        # Return the index
        return int(index)

    def unregister(
        self,
        index: int,
    ) -> None:
        """
        Unregister a node from the storage.

        Args:
            index (int): The index of the node to unregister.
        """

        # Check, if the index is in the index to uuid mapping
        if not self.has_index(index=index):
            # Return, if the index is not in the index to uuid mapping
            return None

        # Get the node for the index
        node: Optional[IndexedLinkedNode] = self.get_node_for_index(index=index)

        # Check, if the node is None
        if node is None:
            # Return, if the node is None
            return None

        # Unregister the node from the index to uuid mapping
        self._index_to_uuid[index] = None

        # Unregister the node from the uuid to node mapping
        self._uuid_to_node[node.identifier] = None

        # Check, if the index is the first index
        if int(index) == 0:
            # Update the head
            self.update_head()

        # Check, if the index is the last index
        if int(index) == self.get_size() - 1:
            # Update the tail
            self.update_tail()

    def update(
        self,
        index: int,
        value: Any,
    ) -> bool:
        """
        Update a node's value.

        Args:
            index (int): The index of the node to update.
            value (Any): The new value of the node.

        Returns:
            bool: True, if the node was updated, False otherwise.
        """

        # Check, if the index is in the index to uuid mapping
        if not self.has_index(index=index):
            # Return, if the index is not in the index to uuid mapping
            return False

        # Get the node for the index
        node: Optional[IndexedLinkedNode] = self.get_node_for_index(index=index)

        # Check, if the node is None
        if node is None:
            # Return, if the node is None
            return False

        # Update the node's value
        node.value = value

        # Return True
        return True

    def update_head(self) -> None:
        """
        Update the head.

        Returns:
            None
        """

        # Get the first used index
        first_used: Optional[int] = self.get_first_used_index()

        # Check, if the first used index is None
        if first_used is None:
            # Return, if the first used index is None
            return None

        # Get the node for the first used index
        node: Optional[IndexedLinkedNode] = self.get_node_for_index(index=first_used)

        # Check, if the node is None
        if node is None:
            # Return, if the node is None
            return None

        # Check, if the head is None
        if self._head is None:
            # Set the head to the node
            self._head = node

            # Return None
            return None

        # Check, if the head is not None and the node is not the head
        if self._head is not None and node != self._head:
            # Set the head to the node
            self._head = node

    def update_tail(self) -> None:
        """
        Update the tail.

        Returns:
            None
        """

        # Get the last used index
        last_used: Optional[int] = self.get_last_used_index()

        # Check, if the last used index is None
        if last_used is None:
            # Return, if the last used index is None
            return None

        # Get the node for the last used index
        node: Optional[IndexedLinkedNode] = self.get_node_for_index(index=last_used)

        # Check, if the node is None
        if node is None:
            # Return, if the node is None
            return None

        # Check, if the tail is None
        if self._tail is None:
            # Set the tail to the node
            self._tail = node

            # Return None
            return None

        # Check, if the tail is not None and the node is not the tail
        if self._tail is not None and node != self._tail:
            # Set the tail to the node
            self._tail = node


class IndexedLinkedList:
    """
    The main class of the IndexedLinkedList.
    """

    def __init__(
        self,
        strict: bool = False,
        *args,
    ) -> None:
        """
        Initialize the list.

        Args:
            strict (bool): Whether to use strict mode.

        Returns:
            None
        """

        # Initialize the storage as an instance of IndexedLinkedNodeStorage
        self._storage: Final[IndexedLinkedNodeStorage] = IndexedLinkedNodeStorage()

        # Store the passed strict mode flag in an immutable variable
        self._strict: Final[bool] = strict

        # Iterate over the passed arguments
        for value in args:
            # Add the value to the list
            self.add(value=value)

    def __getitem__(
        self,
        key: int,
    ) -> Any:
        """
        Get the value at the passed index.

        Args:
            key (int): The index of the value to get.

        Returns:
            Any: The value at the passed index.
        """

        # Get the node for the index
        node: Optional[IndexedLinkedNode] = self._storage.get_node_for_index(index=key)

        # Check, if the node is None
        if node is None:
            # Check, if strict mode is enabled
            self._strict_index_check(index=key)

            # Return None
            return None

        # Return the value of the node
        return node.value

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over the list.

        Returns:
            Iterator[Any]: An iterator over the list.
        """

        # Iterate over the nodes in the storage
        for node in self._storage.nodes():
            # Yield the value of the node
            yield node.value

    def __len__(self) -> int:
        """
        Get the length of the list.

        Returns:
            int: The length of the list.
        """

        # Return the length of the list
        return self._storage.get_size()

    def __setitem__(
        self,
        key: int,
        value: Any,
    ) -> None:
        """
        Set the value at the passed index.

        Args:
            key (int): The index of the value to set.
            value (Any): The value to set.

        Returns:
            None

        Raises:
            IndexError: If the index is out of range.
        """

        # Check, if the index is in the index to uuid mapping
        self._strict_index_check(index=key)

        # Update the node at the index
        self._storage.update(
            index=key,
            value=value,
        )

    @property
    def size(self) -> int:
        """
        Get the size of the list.

        Returns:
            int: The size of the list.
        """

        # Return the size of the list
        return self._storage.get_size()

    @property
    def strict(self) -> bool:
        """
        Get the strict mode flag.

        Returns:
            bool: The strict mode flag.
        """

        # Return the strict mode flag
        return self._strict

    def _strict_index_check(
        self,
        index: int,
    ) -> None:
        """
        Check, if the passed index is in the index to uuid mapping.

        Args:
            index (int): The index to check.

        Returns:
            None

        Raises:
            IndexError: If the index is out of range.
        """

        # Check, if the index is in the index to uuid mapping
        if self.strict and not self._storage.has_index(index=index):
            # Raise an IndexError
            raise IndexError(f"Index {index} out of range.")

    def _strict_value_check(
        self,
        value: Any,
    ) -> None:
        """
        Check, if the passed value is in the list.

        Args:
            value (Any): The value to check.

        Returns:
            None

        Raises:
            ValueError: If the value is not in the list.
        """

        # Check, if the value is in the list
        if self.strict and not self._storage.has_value(value=value):
            # Raise a ValueError
            raise ValueError(f"Value {value} not in list.")

    def add(
        self,
        value: Any,
    ) -> int:
        """
        Add a value to the list.

        Args:
            value (Any): The value to add.

        Returns:
            int: The index of the added value.
        """

        # Initialize the builder as an instance of IndexedLinkedNodeBuilder
        builder: IndexedLinkedNodeBuilder = IndexedLinkedNodeBuilder()

        # Set the identifier of the node
        builder.with_identifier()

        # Set the value of the node
        builder.with_value(value=value)

        # Build the node
        node: IndexedLinkedNode = builder.build()

        # Register the node in the storage and return the index
        return self._storage.register(node=node)

    def get_first(self) -> Optional[Any]:
        """
        Get the first value in the list.

        Returns:
            Optional[Any]: The first value in the list, or None if the list is empty.
        """

        # Get the first used index
        first_used: Optional[int] = self._storage.get_first_used_index()

        # Check, if the first used index is None
        if first_used is None:
            # Return None
            return None

        # Check, if the first used index is out of range
        self._strict_index_check(index=first_used)

        # Return the first value in the list
        node: Optional[IndexedLinkedNode] = self._storage.get_node_for_index(
            index=first_used
        )

        # Check, if the node is None
        if node is None:
            # Return None
            return None

        # Return the first value in the list
        return node.value

    def get_last(self) -> Optional[Any]:
        """
        Get the last value in the list.

        Returns:
            Optional[Any]: The last value in the list, or None if the list is empty.
        """

        # Get the last used index
        last_used: Optional[int] = self._storage.get_last_used_index()

        # Check, if the last used index is None
        if last_used is None:
            # Return None
            return None

        # Check, if the last used index is out of range
        self._strict_index_check(index=last_used)

        # Return the last value in the list
        node: Optional[IndexedLinkedNode] = self._storage.get_node_for_index(
            index=last_used
        )

        # Check, if the node is None
        if node is None:
            # Return None
            return None

        # Return the last value in the list
        return node.value

    def index_of(
        self,
        value: Any,
    ) -> Optional[int]:
        """
        Get the index of a value in the list.

        Args:
            value (Any): The value to get the index of.

        Returns:
            Optional[int]: The index of the value, or None if the value is not in the list.
        """

        # Check, if strict mode is enabled
        self._strict_value_check(value=value)

        # Get the node for the value
        node: Optional[IndexedLinkedNode] = self._storage.get_node_with_value(
            value=value
        )

        # Check, if the node is None
        if node is None:
            # Return None
            return None

        # Return the index of the node
        return self._storage.get_index_of_node(node=node)

    def remove(
        self,
        index: int,
    ) -> None:
        """
        Remove a value from the list.

        Args:
            index (int): The index of the value to remove.

        Returns:
            None
        """

        # Check, if strict mode is enabled
        self._strict_index_check(index=index)

        # Unregister the node from the storage
        self._storage.unregister(index=index)

    def to_dict(self) -> dict[int, Any]:
        """
        Convert the list to a dictionary.

        Returns:
            dict[int, Any]: The dictionary.
        """

        # Return the dictionary
        return {
            index: item
            for (
                index,
                item,
            ) in enumerate(iterable=self.to_list())
        }

    def to_list(self) -> list[Any]:
        """
        Convert the list to a list.

        Returns:
            list[Any]: The list.
        """

        # Return the list
        return [node.value for node in self._storage.get_nodes()]

    def to_set(self) -> set[Any]:
        """
        Convert the list to a set.

        Returns:
            set[Any]: The set.
        """

        # Return the set
        return set(self.to_list())

    def to_tuple(self) -> tuple[Any]:
        """
        Convert the list to a tuple.

        Returns:
            tuple[Any]: The tuple.
        """

        # Return the tuple
        return tuple(self.to_list())

    def update(
        self,
        index: int,
        value: Any,
    ) -> bool:
        """
        Update a value in the list.

        Args:
            index (int): The index of the value to update.
            value (Any): The new value.

        Returns:
            bool: True, if the value was updated, False otherwise.
        """

        # Check, if strict mode is enabled
        self._strict_index_check(index=index)

        # Update the node in the storage
        return self._storage.update(
            index=index,
            value=value,
        )
